from collections import defaultdict
from collections.abc import (
    Mapping,
    Sequence,
)
from enum import StrEnum, auto
from typing import Literal, Self, TypeAlias

from pydantic import Field, model_serializer

from .cards import CardUnit, RawCard
from .config import UNIT_FOLDERS, UNIT_TITLES
from .deck import Deck
from .errors import EmptyUnitCardsError, MediaValidationError
from .html import MissingMedia, NormalizedHtml, normalize_source_links
from .models import FrozenModel


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


class CardAnswer(FrozenModel):
    html: str
    missing_media: MissingMedia = Field(default_factory=MissingMedia, exclude=True)

    @classmethod
    def from_answer_html(cls, html: str) -> Self:
        normalized_html = NormalizedHtml.from_image_links(html)
        return cls(html=normalized_html.html, missing_media=normalized_html.missing_media)


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
    missing_media: MissingMedia = Field(default_factory=MissingMedia, exclude=True)

    @classmethod
    def from_raw_card(cls, card: RawCard) -> Self:
        brief_response = BriefResponseAnswer.from_answer_html(card.answers.brief_response)
        development = DevelopmentAnswer.from_answer_html(card.answers.development)
        nuance = NuanceAnswer.from_answer_html(card.answers.nuance)
        example = ExampleAnswer.from_answer_html(card.answers.example)
        answer_values = (
            brief_response,
            development,
            nuance,
            example,
        )
        missing_media = MissingMedia.from_card_answers(answer_values)
        return cls(
            brief_response=brief_response,
            development=development,
            nuance=nuance,
            example=example,
            missing_media=missing_media,
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
    missing_media: MissingMedia = Field(default_factory=MissingMedia, exclude=True)

    @classmethod
    def from_raw_card(cls, card: RawCard) -> Self:
        question = NormalizedHtml.from_image_links(card.question.html)
        answers = CardAnswers.from_raw_card(card)
        source = NormalizedHtml.from_image_links(card.source.html)
        missing_media = MissingMedia.from_missing_media(
            (question.missing_media, answers.missing_media, source.missing_media)
        )

        return cls(
            id=card.guid.value,
            question_html=question.html,
            answers=answers,
            source_html=normalize_source_links(source.html),
            missing_media=missing_media,
        )


class UnitCardData(FrozenModel):
    title: str
    cards: Sequence[CardOutput]


class FlashcardsData(FrozenModel):
    source: str
    units: Mapping[str, UnitCardData]

    @classmethod
    def from_deck(cls, deck: Deck) -> Self:
        cards_by_unit: defaultdict[CardUnit, list[CardOutput]] = defaultdict(list[CardOutput])
        empty_units = set(UNIT_FOLDERS)

        for card in deck.cards:
            cards_by_unit[card.unit].append(CardOutput.from_raw_card(card))
            empty_units.discard(card.unit.value)

        if empty_units:
            raise EmptyUnitCardsError(empty_units=empty_units)

        units = {
            unit: UnitCardData(
                title=UNIT_TITLES[unit],
                cards=cards_by_unit[CardUnit(value=unit)],
            )
            for unit in UNIT_FOLDERS
        }
        missing_media = MissingMedia.from_unit_cards(units.values())
        if missing_media.filenames:
            raise MediaValidationError(missing_media=missing_media)

        return cls(source="anki_deck.txt", units=units)

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, indent=2) + "\n"
