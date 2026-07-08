from typing import NamedTuple


class AnkiRow(NamedTuple):
    guid: str
    note_type: str
    deck: str
    question_html: str
    brief_response_html: str
    development_html: str
    nuance_html: str
    example_html: str
    source_html: str
    tags: str
