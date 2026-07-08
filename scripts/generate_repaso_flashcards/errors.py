from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .html import MissingMedia


@dataclass(frozen=True)
class FlashcardGenerationError(Exception):
    """Base class for expected flashcard generation failures."""


@dataclass(frozen=True)
class DeckFormatError(FlashcardGenerationError):
    """Raised when the Anki export cannot be parsed as the expected deck format."""


@dataclass(frozen=True)
class MissingDeckHeadersError(DeckFormatError):
    path: Path
    missing_headers: Sequence[str]

    def __str__(self) -> str:
        return f"{self.path} is missing required Anki export headers: {list(self.missing_headers)}"


@dataclass(frozen=True)
class DeckRowFormatError(DeckFormatError):
    path: Path
    line_number: int
    column_count: int

    def __str__(self) -> str:
        return f"{self.path}:{self.line_number} expected 10 columns, found {self.column_count}"


@dataclass(frozen=True)
class CardValidationError(FlashcardGenerationError):
    """Raised when a selected card is incomplete or inconsistent."""


@dataclass(frozen=True)
class EmptyUnitCardsError(CardValidationError):
    empty_units: Sequence[str]

    def __str__(self) -> str:
        return f"Selected deck contains no cards for units: {', '.join(sorted(self.empty_units))}"


@dataclass(frozen=True)
class MediaValidationError(FlashcardGenerationError):
    missing_media: "MissingMedia"

    def __str__(self) -> str:
        missing_list = "\n".join(
            f"- {filename}" for filename in sorted(self.missing_media.filenames)
        )
        return "Flashcard media files are missing from book/assets/flashcards:\n" + missing_list


@dataclass(frozen=True)
class OutputValidationError(FlashcardGenerationError):
    errors: Sequence[str]

    def __str__(self) -> str:
        return (
            "Generated Repaso outputs are stale. Run "
            "`uv run poe generate-repaso-flashcards`.\n\n" + "\n".join(self.errors)
        )
