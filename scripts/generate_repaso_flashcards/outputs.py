from collections.abc import Sequence
from pathlib import Path
from typing import Self

from .config import (
    BOOK_ROOT,
    CARD_DATA_PATH,
    REPASO_PAGE_TEMPLATE,
    REPASO_TARGET_LABELS,
    UNIT_FOLDERS,
)
from .errors import OutputValidationError
from .flashcards import FlashcardsData
from .models import FrozenModel


class GeneratedOutput(FrozenModel):
    path: Path
    text: str


class FlashcardJsonOutput(GeneratedOutput):
    @classmethod
    def from_flashcards_data(cls, data: FlashcardsData) -> Self:
        return cls(path=CARD_DATA_PATH, text=data.to_json())


class RepasoPageOutput(GeneratedOutput):
    @staticmethod
    def repaso_page(unit: str, target_label: str, card_count: int) -> str:
        return REPASO_PAGE_TEMPLATE.format(
            card_count=card_count,
            target_label=target_label,
            unit=unit,
        )

    @classmethod
    def from_card_count(cls, unit: str, folder: str, card_count: int) -> Self:
        target_label = REPASO_TARGET_LABELS[unit]
        path = BOOK_ROOT / "chapters" / folder / "repaso.md"
        text = cls.repaso_page(unit=unit, target_label=target_label, card_count=card_count)
        return cls(path=path, text=text)


class GeneratedOutputs(FrozenModel):
    outputs: Sequence[GeneratedOutput]

    @classmethod
    def from_flashcards_data(cls, data: FlashcardsData) -> Self:
        outputs: list[GeneratedOutput] = [FlashcardJsonOutput.from_flashcards_data(data)]

        for unit, folder in UNIT_FOLDERS.items():
            unit_data = data.units[unit]
            repaso_output = RepasoPageOutput.from_card_count(
                unit=unit,
                folder=folder,
                card_count=len(unit_data.cards),
            )
            outputs.append(repaso_output)

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

    def assert_current(self) -> None:
        errors = self.check_errors()
        if errors:
            raise OutputValidationError(errors=errors)

    def write(self) -> None:
        for output in self.outputs:
            output.path.parent.mkdir(parents=True, exist_ok=True)
            if output.path.exists() and output.path.read_text(encoding="utf-8") == output.text:
                continue
            output.path.write_text(output.text, encoding="utf-8", newline="\n")
