import csv
from collections.abc import Sequence
from pathlib import Path
from typing import Self

from .cards import RawCard, SelectedCards
from .config import REQUIRED_HEADERS
from .errors import (
    DeckRowFormatError,
    MissingDeckHeadersError,
)
from .models import FrozenModel
from .row import AnkiRow


class Deck(FrozenModel):
    cards: SelectedCards

    @classmethod
    def from_lines(cls, path: Path, lines: Sequence[str]) -> Self:
        missing_headers = sorted(REQUIRED_HEADERS - set(lines[:6]))
        if missing_headers:
            raise MissingDeckHeadersError(path=path, missing_headers=missing_headers)

        cards = cls.cards_from_lines(path=path, lines=lines)
        return cls(cards=cards)

    @classmethod
    def cards_from_lines(cls, path: Path, lines: Sequence[str]) -> list[RawCard]:
        cards: list[RawCard] = []
        reader = csv.reader(lines[6:], delimiter="\t", quotechar='"')
        for line_number, row in enumerate(reader, start=7):
            if not row:
                continue
            if len(row) != 10:
                raise DeckRowFormatError(path=path, line_number=line_number, column_count=len(row))

            anki_row = AnkiRow(*row)
            card = RawCard.from_row(anki_row)
            if card is not None:
                cards.append(card)

        return list(cards)
