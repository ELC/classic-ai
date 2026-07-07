from __future__ import annotations

import argparse
import csv
import re
import sys
from collections.abc import (
    Mapping,
    MutableMapping,
    MutableSequence,
    Sequence,
    Set as AbstractSet,
)
from enum import StrEnum, auto
from pathlib import Path
from typing import Literal, Self, TypeAlias

from pydantic import BaseModel, ConfigDict, Field, model_serializer


REPO_ROOT = Path(__file__).resolve().parents[1]
ANKI_DECK_PATH = REPO_ROOT / "anki_deck.txt"
BOOK_ROOT = REPO_ROOT / "book"
CARD_DATA_PATH = BOOK_ROOT / "data" / "flashcards.json"
FLASHCARD_MEDIA_DIR = BOOK_ROOT / "assets" / "flashcards"
SOURCE_BASE_URL = "https://elc.github.io/classic-ai/"

UNIT_FOLDERS: Mapping[str, str] = {
    "01": "unit-01-introduccion",
    "02": "unit-02-busqueda-y-planificacion",
    "03": "unit-03-representacion-conocimiento",
    "04": "unit-04-ingenieria-conocimiento",
    "05": "unit-05-redes-neuronales",
}
UNIT_TITLES: Mapping[str, str] = {
    "01": "Unidad 1: Introducción a la inteligencia artificial",
    "02": "Unidad 2: Búsqueda y planificación",
    "03": "Unidad 3: Representación del conocimiento y razonamiento",
    "04": "Unidad 4: Ingeniería del conocimiento",
    "05": "Unidad 5: Redes neuronales",
}
REQUIRED_HEADERS: AbstractSet[str] = frozenset(
    {
        "#separator:tab",
        "#html:true",
        "#guid column:1",
        "#notetype column:2",
        "#deck column:3",
        "#tags column:10",
    }
)

IMAGE_SRC_PATTERN = re.compile(r"(<img\b[^>]*?\bsrc=)([\"'])([^\"']+)([\"'])", re.IGNORECASE)
HREF_PATTERN = re.compile(r"(<a\b[^>]*?\bhref=)([\"'])([^\"']+)([\"'])", re.IGNORECASE)
REPASO_PAGE_TEMPLATE = """---
title: Repaso
---

# Repaso

<!--
Archivo generado automáticamente desde ../../../anki_deck.txt.
No editar a mano: actualizá el mazo exportado y ejecutá el generador.
-->

Estas tarjetas de repaso se generan desde el mazo Anki exportado para esta
unidad. Usalas para practicar respuestas orales: primero intentá responder y
después revelá la respuesta completa con su fuente.

Tarjetas disponibles: {card_count}.

:::{{flashcards-{unit}}} :::
"""


class FrozenModel(BaseModel):
    model_config = ConfigDict(frozen=True)


class SentenceCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: Sequence[str]) -> str:
        return name.replace("_", " ").lower().capitalize()


class AnswerLabel(SentenceCaseStrEnum):
    RESPUESTA_BREVE = auto()
    DESARROLLO = auto()
    MATIZ = auto()
    EJEMPLO = auto()


ANSWER_LABELS: Sequence[AnswerLabel] = list(AnswerLabel)


class RawCard(FrozenModel):
    guid: str
    unit: str
    question_html: str
    answer_html: Sequence[str]
    source_html: str
    tags: Sequence[str]
    line_number: int

    @classmethod
    def from_line(cls, path: Path, line_number: int, row: Sequence[str]) -> Self | None:
        if not row:
            return None
        if len(row) != 10:
            raise ValueError(f"{path}:{line_number} expected 10 columns, found {len(row)}")

        tags = cls.normalized_tags(row[9])
        unit = cls.selected_unit(tags)
        if unit is None or cls.has_faq_tag(tags):
            return None

        answers = [row[4].strip(), row[5].strip(), row[6].strip(), row[7].strip()]
        if any(not answer for answer in answers):
            raise ValueError(
                f"{path}:{line_number} selected card {row[0]!r} must include all four "
                "answer fields"
            )

        question = row[3].strip()
        source = row[8].strip()
        if not question:
            raise ValueError(f"{path}:{line_number} selected card {row[0]!r} is missing a question")
        if not source:
            raise ValueError(f"{path}:{line_number} selected card {row[0]!r} is missing a source")

        return cls(
            guid=row[0],
            unit=unit,
            question_html=question,
            answer_html=answers,
            source_html=source,
            tags=tags,
            line_number=line_number,
        )

    @staticmethod
    def normalized_tags(tags_field: str) -> list[str]:
        return [tag for tag in tags_field.split() if tag]

    @staticmethod
    def selected_unit(tags: Sequence[str]) -> str | None:
        for unit in UNIT_FOLDERS:
            if f"unit_{unit}" in tags:
                return unit
        return None

    @staticmethod
    def has_faq_tag(tags: Sequence[str]) -> bool:
        return "ia_faq" in tags or any(tag.startswith("faq_capitulo_") for tag in tags)


class Deck(FrozenModel):
    cards: Sequence[RawCard]

    @classmethod
    def from_file(cls, path: Path) -> Self:
        lines = path.read_text(encoding="utf-8").splitlines()
        missing_headers = sorted(REQUIRED_HEADERS - set(lines[:6]))
        if missing_headers:
            raise ValueError(f"{path} is missing required Anki export headers: {missing_headers}")

        cards: MutableSequence[RawCard] = []
        reader = csv.reader(lines[6:], delimiter="\t", quotechar='"')
        for line_number, row in enumerate(reader, start=7):
            card = RawCard.from_line(path, line_number, row)
            if card is not None:
                cards.append(card)

        return cls(cards=cards)


class NormalizedHtml(FrozenModel):
    html: str
    missing_media: AbstractSet[str] = Field(default_factory=frozenset[str])

    @classmethod
    def from_image_links(cls, html: str) -> Self:
        missing_media: set[str] = set()

        def replace(match: re.Match[str]) -> str:
            prefix, quote, src, _closing_quote = match.groups()
            if "://" in src or src.startswith(("/", "#", "data:")):
                return match.group(0)

            filename = Path(src).name
            media_path = FLASHCARD_MEDIA_DIR / filename
            if not media_path.is_file():
                missing_media.add(filename)
            return (
                f'{prefix}{quote}/assets/flashcards/{filename}{quote} '
                f'data-flashcard-media="{filename}"'
            )

        return cls(html=IMAGE_SRC_PATTERN.sub(replace, html), missing_media=frozenset(missing_media))


class CardAnswer(FrozenModel):
    html: str


class BriefResponseAnswer(CardAnswer):
    label: Literal[AnswerLabel.RESPUESTA_BREVE] = AnswerLabel.RESPUESTA_BREVE


class DevelopmentAnswer(CardAnswer):
    label: Literal[AnswerLabel.DESARROLLO] = AnswerLabel.DESARROLLO


class NuanceAnswer(CardAnswer):
    label: Literal[AnswerLabel.MATIZ] = AnswerLabel.MATIZ


class ExampleAnswer(CardAnswer):
    label: Literal[AnswerLabel.EJEMPLO] = AnswerLabel.EJEMPLO


CardAnswerUnion: TypeAlias = BriefResponseAnswer | DevelopmentAnswer | NuanceAnswer | ExampleAnswer


class CardAnswers(FrozenModel):
    brief_response: BriefResponseAnswer
    development: DevelopmentAnswer
    nuance: NuanceAnswer
    example: ExampleAnswer
    missing_media: AbstractSet[str] = Field(default_factory=frozenset[str], exclude=True)

    @classmethod
    def from_raw_card(cls, card: RawCard) -> Self:
        normalized_answers = [
            NormalizedHtml.from_image_links(answer) for answer in card.answer_html
        ]
        html_fields = [answer.html for answer in normalized_answers]
        expected_count = len(ANSWER_LABELS)
        if len(html_fields) != expected_count:
            raise ValueError(f"Expected {expected_count} answer fields, found {len(html_fields)}")

        brief_response, development, nuance, example = html_fields
        return cls(
            brief_response=BriefResponseAnswer(html=brief_response),
            development=DevelopmentAnswer(html=development),
            nuance=NuanceAnswer(html=nuance),
            example=ExampleAnswer(html=example),
            missing_media=frozenset(
                filename
                for normalized_answer in normalized_answers
                for filename in normalized_answer.missing_media
            ),
        )

    @model_serializer
    def serialize_model(
        self,
    ) -> tuple[BriefResponseAnswer, DevelopmentAnswer, NuanceAnswer, ExampleAnswer]:
        return (self.brief_response, self.development, self.nuance, self.example)


class CardOutput(FrozenModel):
    id: str
    question_html: str = Field(serialization_alias="questionHtml")
    answers: CardAnswers
    source_html: str = Field(serialization_alias="sourceHtml")
    missing_media: AbstractSet[str] = Field(default_factory=frozenset[str], exclude=True)

    @classmethod
    def from_raw_card(cls, card: RawCard) -> Self:
        question = NormalizedHtml.from_image_links(card.question_html)
        answers = CardAnswers.from_raw_card(card)
        source = NormalizedHtml.from_image_links(card.source_html)
        missing_media = frozenset(
            (*question.missing_media, *answers.missing_media, *source.missing_media)
        )

        return cls(
            id=card.guid,
            question_html=question.html,
            answers=answers,
            source_html=cls.normalize_source_links(source.html),
            missing_media=missing_media,
        )

    @staticmethod
    def normalized_book_path(url: str) -> str | None:
        if not url.startswith(SOURCE_BASE_URL):
            return None
        return url.removeprefix(SOURCE_BASE_URL).lstrip("/")

    @staticmethod
    def normalize_source_links(html: str) -> str:
        def replace(match: re.Match[str]) -> str:
            prefix, quote, href, _closing_quote = match.groups()
            book_path = CardOutput.normalized_book_path(href)
            if book_path is None:
                return match.group(0)
            return f'{prefix}{quote}/{book_path}{quote} data-book-path="{book_path}"'

        return HREF_PATTERN.sub(replace, html)


class UnitCardData(FrozenModel):
    title: str
    cards: Sequence[CardOutput]


class FlashcardsData(FrozenModel):
    source: str
    units: Mapping[str, UnitCardData]

    @classmethod
    def from_deck(cls, deck: Deck) -> Self:
        cards_by_unit: MutableMapping[str, MutableSequence[CardOutput]] = {
            unit: [] for unit in UNIT_FOLDERS
        }

        for card in deck.cards:
            cards_by_unit[card.unit].append(CardOutput.from_raw_card(card))

        empty_units = [unit for unit, unit_cards in cards_by_unit.items() if not unit_cards]
        if empty_units:
            raise ValueError(f"Selected deck contains no cards for units: {', '.join(empty_units)}")

        missing_media = frozenset(
            filename
            for unit_cards in cards_by_unit.values()
            for card in unit_cards
            for filename in card.missing_media
        )
        if missing_media:
            missing_list = "\n".join(f"- {filename}" for filename in sorted(missing_media))
            raise ValueError(
                "Flashcard media files are missing from book/assets/flashcards:\n" + missing_list
            )

        units = {
            unit: UnitCardData(title=UNIT_TITLES[unit], cards=unit_cards)
            for unit, unit_cards in cards_by_unit.items()
        }
        return cls(source="anki_deck.txt", units=units)

    @staticmethod
    def generated_page(unit: str, card_count: int) -> str:
        return REPASO_PAGE_TEMPLATE.format(card_count=card_count, unit=unit)

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, indent=2) + "\n"


class GeneratedOutput(FrozenModel):
    path: Path
    text: str


class GeneratedOutputs(FrozenModel):
    outputs: Sequence[GeneratedOutput]

    @classmethod
    def from_flashcards_data(cls, data: FlashcardsData) -> Self:
        outputs = [GeneratedOutput(path=CARD_DATA_PATH, text=data.to_json())]

        for unit, folder in UNIT_FOLDERS.items():
            unit_data = data.units[unit]
            path = BOOK_ROOT / "chapters" / folder / "repaso.md"
            outputs.append(
                GeneratedOutput(
                    path=path,
                    text=FlashcardsData.generated_page(unit, len(unit_data.cards)),
                )
            )

        return cls(outputs=outputs)

    def check_errors(self) -> list[str]:
        errors: list[str] = []
        for output in self.outputs:
            message = self.check_output(output)
            if message is not None:
                errors.append(message)
        return errors

    @staticmethod
    def check_output(output: GeneratedOutput) -> str | None:
        if not output.path.exists():
            return f"{output.path} does not exist"
        existing = output.path.read_text(encoding="utf-8")
        if existing != output.text:
            return f"{output.path} is stale"
        return None

    def write(self) -> None:
        for output in self.outputs:
            output.path.parent.mkdir(parents=True, exist_ok=True)
            if output.path.exists() and output.path.read_text(encoding="utf-8") == output.text:
                continue
            output.path.write_text(output.text, encoding="utf-8", newline="\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Repaso flashcard pages and data from an Anki TSV export."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if generated files are stale without writing updates.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        deck = Deck.from_file(ANKI_DECK_PATH)
        data = FlashcardsData.from_deck(deck)
        outputs = GeneratedOutputs.from_flashcards_data(data)

        if args.check:
            errors = outputs.check_errors()
            if errors:
                print(
                    "Generated Repaso outputs are stale. Run "
                    "`uv run poe generate-repaso-flashcards`.\n\n" + "\n".join(errors),
                    file=sys.stderr,
                )
                return 1
            return 0

        outputs.write()
    except (TypeError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
