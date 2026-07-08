import typer
from pydantic import ValidationError

from .config import ANKI_DECK_PATH
from .deck import Deck
from .errors import FlashcardGenerationError
from .flashcards import FlashcardsData
from .outputs import GeneratedOutputs


app = typer.Typer(
    help="Generate Repaso flashcard pages and data from an Anki TSV export.",
    no_args_is_help=True,
)


def generated_outputs() -> GeneratedOutputs:
    lines = ANKI_DECK_PATH.read_text(encoding="utf-8").splitlines()
    deck = Deck.from_lines(path=ANKI_DECK_PATH, lines=lines)
    data = FlashcardsData.from_deck(deck)
    return GeneratedOutputs.from_flashcards_data(data)


@app.command()
def generate() -> None:
    """Write generated Repaso flashcard pages and JSON data."""
    try:
        generated_outputs().write()
    except (FlashcardGenerationError, ValidationError) as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(1) from error


@app.command()
def check() -> None:
    """Fail if generated Repaso outputs are stale."""
    try:
        generated_outputs().assert_current()
    except (FlashcardGenerationError, ValidationError) as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(1) from error


def main() -> int:
    try:
        app()
    except SystemExit as error:
        return int(error.code or 0)
    return 0
