from collections.abc import Mapping, Set as AbstractSet
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
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
REPASO_TARGET_LABELS: Mapping[str, str] = {
    "01": "repaso",
    "02": "repaso-2",
    "03": "repaso-3",
    "04": "repaso-4",
    "05": "repaso-5",
}
REPASO_PAGE_TEMPLATE = """---
title: Repaso
---

({target_label})=

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
