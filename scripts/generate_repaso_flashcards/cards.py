from collections.abc import Sequence
from typing import Annotated, Self

from pydantic import ConfigDict, Field

from .config import UNIT_FOLDERS
from .models import FrozenModel
from .row import AnkiRow

NonEmptyHtml = Annotated[str, Field(min_length=1)]


class CardValue(FrozenModel):
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True)


class CardGuid(CardValue):
    value: str


class CardQuestion(CardValue):
    html: NonEmptyHtml


class CardAnswers(CardValue):
    brief_response: NonEmptyHtml
    development: NonEmptyHtml
    nuance: NonEmptyHtml
    example: NonEmptyHtml


class CardSource(CardValue):
    html: NonEmptyHtml


class CardTags(CardValue):
    values: Sequence[str]

    def has_faq_tag(self) -> bool:
        return "ia_faq" in self.values or any(
            tag.startswith("faq_capitulo_") for tag in self.values
        )


class CardUnit(CardValue):
    value: str

    @classmethod
    def from_tags(cls, tags: CardTags) -> Self | None:
        if tags.has_faq_tag():
            return None
        for unit in UNIT_FOLDERS:
            if f"unit_{unit}" in tags.values:
                return cls(value=unit)
        return None


class RawCard(FrozenModel):
    guid: CardGuid
    unit: CardUnit
    question: CardQuestion
    answers: CardAnswers
    source: CardSource
    tags: CardTags

    @classmethod
    def from_row(cls, row: AnkiRow) -> Self | None:
        tags = CardTags(values=[tag for tag in row.tags.split() if tag])
        unit = CardUnit.from_tags(tags)
        if unit is None:
            return None

        guid = CardGuid(value=row.guid)
        answers = CardAnswers(
            brief_response=row.brief_response_html,
            development=row.development_html,
            nuance=row.nuance_html,
            example=row.example_html,
        )
        question = CardQuestion(html=row.question_html)
        source = CardSource(html=row.source_html)

        return cls(
            guid=guid,
            unit=unit,
            question=question,
            answers=answers,
            source=source,
            tags=tags,
        )


SelectedCards = Annotated[list[RawCard], Field(min_length=1)]
