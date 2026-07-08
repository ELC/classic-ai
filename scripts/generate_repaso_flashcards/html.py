import re
from collections.abc import Iterable, Sequence, Set as AbstractSet
from pathlib import Path
from typing import TYPE_CHECKING, Self

from pydantic import Field

from .config import FLASHCARD_MEDIA_DIR, SOURCE_BASE_URL
from .models import FrozenModel

if TYPE_CHECKING:
    from .flashcards import CardAnswer
    from .flashcards import CardOutput
    from .flashcards import UnitCardData


IMAGE_SRC_PATTERN = re.compile(r"(<img\b[^>]*?\bsrc=)([\"'])([^\"']+)([\"'])", re.IGNORECASE)
HREF_PATTERN = re.compile(r"(<a\b[^>]*?\bhref=)([\"'])([^\"']+)([\"'])", re.IGNORECASE)


class MissingMedia(FrozenModel):
    filenames: AbstractSet[str] = Field(default_factory=frozenset[str])

    @classmethod
    def from_filenames(cls, filenames: Iterable[str]) -> Self:
        return cls(filenames=frozenset(filenames))

    @classmethod
    def from_missing_media(cls, missing_media_values: Iterable["MissingMedia"]) -> Self:
        return cls.from_filenames(
            filename
            for missing_media in missing_media_values
            for filename in missing_media.filenames
        )

    @classmethod
    def from_card_answers(cls, answers: Sequence["CardAnswer"]) -> Self:
        return cls.from_missing_media(answer.missing_media for answer in answers)

    @classmethod
    def from_cards(cls, cards: Iterable["CardOutput"]) -> Self:
        return cls.from_missing_media(card.missing_media for card in cards)

    @classmethod
    def from_unit_cards(cls, units: Iterable["UnitCardData"]) -> Self:
        return cls.from_cards(card for unit in units for card in unit.cards)


class NormalizedHtml(FrozenModel):
    html: str
    missing_media: MissingMedia = Field(default_factory=MissingMedia)

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
                f"{prefix}{quote}/assets/flashcards/{filename}{quote} "
                f'data-flashcard-media="{filename}"'
            )

        return cls(
            html=IMAGE_SRC_PATTERN.sub(replace, html),
            missing_media=MissingMedia.from_filenames(missing_media),
        )


def normalized_book_path(url: str) -> str | None:
    if not url.startswith(SOURCE_BASE_URL):
        return None
    return url.removeprefix(SOURCE_BASE_URL).lstrip("/")


def normalize_source_link_match(match: re.Match[str]) -> str:
    prefix, quote, href, _closing_quote = match.groups()
    book_path = normalized_book_path(href)
    if book_path is None:
        return match.group(0)
    return f'{prefix}{quote}/{book_path}{quote} data-book-path="{book_path}"'


def normalize_source_links(html: str) -> str:
    return HREF_PATTERN.sub(normalize_source_link_match, html)
