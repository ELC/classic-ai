from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast
from urllib.parse import unquote, urldefrag, urljoin, urlparse

from selectolax.lexbor import LexborHTMLParser


REPO_ROOT = Path(__file__).resolve().parents[1]
BOOK_ROOT = REPO_ROOT / "book"
CHAPTERS_ROOT = BOOK_ROOT / "chapters"
HTML_ROOT = BOOK_ROOT / "_build" / "html"
CARD_DATA_PATH = BOOK_ROOT / "data" / "flashcards.json"
MYST_CONFIG = BOOK_ROOT / "myst.yml"
SAME_BOOK_URL_PREFIX = "https://elc.github.io/classic-ai/"
SAME_BOOK_BASE_PATH = "/classic-ai"
MAX_ROUTE_SEGMENT_LENGTH = 50
FLASHCARD_SYNC_MESSAGE = (
    "Re-sync Anki with the canonical chapter links, then run "
    "`uv run poe generate-repaso-flashcards`."
)

TOC_FILE_PATTERN = re.compile(r"^\s*-\s+file:\s+(chapters/[^\s#]+\.md)\s*$")
TARGET_PATTERN = re.compile(r"^\(([^)]+)\)=\s*$")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LINK_PATTERN = re.compile(r"(!?)\[([^\]\n]*)\]\(([^)\n]+)\)")
LEADING_NUMBER_PATTERN = re.compile(r"^\d+-")
ASSET_EXTENSIONS = {
    ".avif",
    ".css",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".pdf",
    ".png",
    ".svg",
    ".webp",
}
GENERATED_FRAGMENT_EXCEPTIONS = frozenset(
    {
        "references",
        "skip-to-article",
        "skip-to-frontmatter",
    }
)


@dataclass(frozen=True)
class Heading:
    path: Path
    line_index: int
    level: int
    text: str
    base_label: str
    label: str


@dataclass(frozen=True)
class ChapterPage:
    path: Path
    route: str
    headings: tuple[Heading, ...]

    @property
    def h1_label(self) -> str:
        for heading in self.headings:
            if heading.level == 1:
                return heading.label
        if self.headings:
            return self.headings[0].label
        raise ValueError(f"{self.path} has no headings")

    @property
    def labels(self) -> set[str]:
        return {heading.label for heading in self.headings}

    @property
    def labels_by_base(self) -> dict[str, list[str]]:
        labels: dict[str, list[str]] = {}
        for heading in self.headings:
            labels.setdefault(heading.base_label, []).append(heading.label)
        return labels


@dataclass(frozen=True)
class LinkRewrite:
    url: str
    errors: tuple[str, ...] = ()


def slugify(text: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text.lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "section"


def visible_heading_text(text: str) -> str:
    text = re.sub(r"\s+\{#[^}]+\}\s*$", "", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"</?[^>]+>", "", text)
    text = text.replace("*", "").replace("_", "").replace("~", "")
    return text.strip()


def is_fence(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def heading_match(line: str) -> re.Match[str] | None:
    match = HEADING_PATTERN.match(line)
    if match is None:
        return None
    _marker, text = match.groups()
    if not text.strip():
        return None
    return match


def toc_paths() -> list[Path]:
    paths: list[Path] = []
    for line in MYST_CONFIG.read_text(encoding="utf-8").splitlines():
        match = TOC_FILE_PATTERN.match(line)
        if match is None:
            continue
        paths.append((BOOK_ROOT / match.group(1)).resolve())
    return paths


def chapter_paths() -> list[Path]:
    ordered: list[Path] = []
    seen: set[Path] = set()
    for path in toc_paths():
        if path.is_file() and path not in seen:
            ordered.append(path)
            seen.add(path)
    for path in sorted(CHAPTERS_ROOT.rglob("*.md")):
        resolved = path.resolve()
        if resolved not in seen:
            ordered.append(resolved)
            seen.add(resolved)
    return ordered


def route_segment_from_stem(stem: str) -> str:
    slug = slugify(LEADING_NUMBER_PATTERN.sub("", stem))
    return slug[:MAX_ROUTE_SEGMENT_LENGTH].rstrip("-")


def canonical_route(path: Path) -> str:
    relative = path.relative_to(BOOK_ROOT).with_suffix("")
    parts = list(relative.parts)
    parts[-1] = route_segment_from_stem(parts[-1])
    return "/" + "/".join(part.replace("\\", "/") for part in parts) + "/"


def route_aliases(path: Path, route: str) -> set[str]:
    relative = path.relative_to(BOOK_ROOT)
    no_suffix = relative.with_suffix("").as_posix()
    aliases = {
        route.strip("/"),
        no_suffix,
        relative.as_posix(),
    }
    parts = list(relative.with_suffix("").parts)
    parts[-1] = slugify(LEADING_NUMBER_PATTERN.sub("", parts[-1]))
    aliases.add("/".join(parts))
    return aliases


def collect_heading_stubs(paths: list[Path]) -> dict[Path, list[tuple[int, int, str, str]]]:
    stubs: dict[Path, list[tuple[int, int, str, str]]] = {}
    for path in paths:
        lines = path.read_text(encoding="utf-8").splitlines()
        in_fence = False
        page_stubs: list[tuple[int, int, str, str]] = []
        for line_index, line in enumerate(lines):
            if is_fence(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            match = heading_match(line)
            if match is None:
                continue
            marker, text = match.groups()
            clean_text = visible_heading_text(text)
            page_stubs.append((line_index, len(marker), clean_text, slugify(clean_text)))
        stubs[path] = page_stubs
    return stubs


def build_pages(paths: list[Path]) -> dict[Path, ChapterPage]:
    stubs = collect_heading_stubs(paths)
    counts: dict[str, int] = {}
    pages: dict[Path, ChapterPage] = {}
    for path in paths:
        headings: list[Heading] = []
        for line_index, level, text, base_label in stubs[path]:
            counts[base_label] = counts.get(base_label, 0) + 1
            label = base_label if counts[base_label] == 1 else f"{base_label}-{counts[base_label]}"
            headings.append(
                Heading(
                    path=path,
                    line_index=line_index,
                    level=level,
                    text=text,
                    base_label=base_label,
                    label=label,
                )
            )
        pages[path] = ChapterPage(path=path, route=canonical_route(path), headings=tuple(headings))
    return pages


def target_block_heading_index(lines: list[str], line_index: int) -> int | None:
    if TARGET_PATTERN.match(lines[line_index]) is None:
        return None
    next_index = line_index + 1
    while next_index < len(lines) and (
        TARGET_PATTERN.match(lines[next_index]) is not None or not lines[next_index].strip()
    ):
        next_index += 1
    if next_index < len(lines) and heading_match(lines[next_index]) is not None:
        return next_index
    return None


def insert_explicit_targets(page: ChapterPage, lines: list[str]) -> list[str]:
    labels_by_line = {heading.line_index: heading.label for heading in page.headings}
    output: list[str] = []
    in_fence = False
    line_index = 0
    while line_index < len(lines):
        line = lines[line_index]
        if is_fence(line):
            in_fence = not in_fence
            output.append(line)
            line_index += 1
            continue
        target_heading_index = (
            target_block_heading_index(lines, line_index) if not in_fence else None
        )
        if target_heading_index is not None:
            line_index = target_heading_index
            continue
        if not in_fence and line_index in labels_by_line:
            output.append(f"({labels_by_line[line_index]})=")
            output.append("")
            output.append(line)
            line_index += 1
            continue
        output.append(line)
        line_index += 1
    return output


def route_map(pages: dict[Path, ChapterPage]) -> dict[str, ChapterPage]:
    routes: dict[str, ChapterPage] = {}
    for page in pages.values():
        for alias in route_aliases(page.path, page.route):
            routes[alias] = page
    return routes


def is_external_url(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.scheme) and not url.startswith(SAME_BOOK_URL_PREFIX)


def is_asset_link(url: str) -> bool:
    path = urldefrag(url)[0].split("?", maxsplit=1)[0]
    if path.startswith(("images/", "../images/", "./images/")):
        return True
    return Path(path).suffix.lower() in ASSET_EXTENSIONS


def normalize_same_book_url(url: str) -> str:
    if url.startswith(SAME_BOOK_URL_PREFIX):
        return "/" + url.removeprefix(SAME_BOOK_URL_PREFIX).lstrip("/")
    if url.startswith(f"{SAME_BOOK_BASE_PATH}/chapters/"):
        return url.removeprefix(SAME_BOOK_BASE_PATH)
    return url


def page_from_url(
    url: str,
    current_page: ChapterPage,
    routes: dict[str, ChapterPage],
) -> ChapterPage | None:
    normalized = normalize_same_book_url(url)
    path_part = urldefrag(normalized)[0].split("?", maxsplit=1)[0]
    if path_part.startswith("/chapters/"):
        return routes.get(path_part.strip("/").rstrip("/"))
    if path_part.endswith(".md"):
        candidate = (current_page.path.parent / path_part).resolve()
        return routes.get(candidate.relative_to(BOOK_ROOT).as_posix())
    candidate = (current_page.path.parent / f"{path_part}.md").resolve()
    try:
        return routes.get(candidate.relative_to(BOOK_ROOT).as_posix())
    except ValueError:
        return None


def resolve_fragment(
    page: ChapterPage, fragment: str, link_text: str
) -> tuple[str | None, str | None]:
    decoded_fragment = unquote(fragment).strip()
    candidates = [decoded_fragment, slugify(decoded_fragment)]
    if link_text.strip():
        candidates.append(slugify(visible_heading_text(link_text)))
    for candidate in candidates:
        if candidate in page.labels:
            return candidate, None
        labels = page.labels_by_base.get(candidate)
        if labels is None:
            continue
        if len(labels) == 1:
            return labels[0], None
        return None, f"ambiguous fragment #{fragment}; candidates: {', '.join(labels)}"
    return None, f"fragment #{fragment} does not match a heading target"


def rewrite_link(
    path: Path,
    line_number: int,
    current_page: ChapterPage,
    routes: dict[str, ChapterPage],
    marker: str,
    link_text: str,
    raw_url: str,
) -> LinkRewrite:
    if marker == "!" or is_asset_link(raw_url):
        return LinkRewrite(raw_url)
    if raw_url.startswith("#"):
        label, error = resolve_fragment(current_page, raw_url[1:], link_text)
        if error is not None:
            return LinkRewrite(raw_url, (f"{path}:{line_number} {raw_url}: {error}",))
        return LinkRewrite(f"#{label}")
    if is_external_url(raw_url):
        return LinkRewrite(raw_url)

    normalized = normalize_same_book_url(raw_url)
    path_part, fragment = urldefrag(normalized)
    target_page = page_from_url(normalized, current_page, routes)
    if target_page is None:
        return LinkRewrite(
            raw_url,
            (f"{path}:{line_number} {raw_url}: could not resolve internal chapter page",),
        )

    if "%" in raw_url:
        fragment = unquote(fragment)
    if fragment:
        label, error = resolve_fragment(target_page, fragment, link_text)
        if error is not None:
            return LinkRewrite(raw_url, (f"{path}:{line_number} {raw_url}: {error}",))
    elif path_part:
        label = target_page.h1_label
    else:
        label = current_page.h1_label

    return LinkRewrite(f"{target_page.route}#{label}")


def rewrite_links_in_line(
    path: Path,
    line_number: int,
    line: str,
    current_page: ChapterPage,
    routes: dict[str, ChapterPage],
) -> tuple[str, list[str]]:
    errors: list[str] = []

    def replace(match: re.Match[str]) -> str:
        marker, text, raw_url = match.groups()
        rewrite = rewrite_link(
            path, line_number, current_page, routes, marker, text, raw_url.strip()
        )
        errors.extend(rewrite.errors)
        return f"{marker}[{text}]({rewrite.url})"

    return LINK_PATTERN.sub(replace, line), errors


def rewrite_page_source(
    page: ChapterPage, routes: dict[str, ChapterPage]
) -> tuple[bool, list[str]]:
    original = page.path.read_text(encoding="utf-8")
    lines = insert_explicit_targets(page, original.splitlines())
    output: list[str] = []
    errors: list[str] = []
    in_fence = False
    for line_number, line in enumerate(lines, start=1):
        if is_fence(line):
            in_fence = not in_fence
            output.append(line)
            continue
        if in_fence:
            output.append(line)
            continue
        rewritten, line_errors = rewrite_links_in_line(
            page.path,
            line_number,
            line,
            page,
            routes,
        )
        output.append(rewritten)
        errors.extend(line_errors)
    updated = "\n".join(output) + "\n"
    if updated != original:
        page.path.write_text(updated, encoding="utf-8", newline="\n")
        return True, errors
    return False, errors


def html_files() -> list[Path]:
    if not HTML_ROOT.exists():
        return []
    return sorted(HTML_ROOT.rglob("*.html"))


def html_route(path: Path) -> str:
    relative = path.relative_to(HTML_ROOT).as_posix()
    if relative.endswith("/index.html"):
        return "/" + relative[: -len("index.html")]
    return "/" + relative


def target_html_path(path: str) -> Path:
    normalized = path.removeprefix(SAME_BOOK_BASE_PATH)
    if normalized.endswith("/"):
        return HTML_ROOT / normalized.lstrip("/") / "index.html"
    if normalized.endswith(".html"):
        return HTML_ROOT / normalized.lstrip("/")
    return HTML_ROOT / normalized.lstrip("/") / "index.html"


def json_path_for_html(path: Path) -> Path:
    relative = path.relative_to(HTML_ROOT).as_posix()
    if relative.endswith("/index.html"):
        route = relative[: -len("/index.html")]
    else:
        route = relative.removesuffix(".html")
    return HTML_ROOT / f"{route.replace('/', '.')}.json"


def collect_json_ids(path: Path, page: ChapterPage | None) -> set[str]:
    ids: set[str] = set(page.labels) if page is not None else set()
    json_path = json_path_for_html(path)
    if not json_path.is_file():
        return ids

    data = cast(dict[str, Any], json.loads(json_path.read_text(encoding="utf-8")))
    mdast = data.get("mdast", {})
    if isinstance(mdast, dict):
        raw_children = cast(dict[str, Any], mdast).get("children", [])
        children: list[Any] = (
            cast(list[Any], raw_children) if isinstance(raw_children, list) else []
        )
    else:
        children = []
    stack: list[Any] = list(children)
    while stack:
        node = stack.pop()
        if not isinstance(node, dict):
            continue
        typed_node = cast(dict[str, Any], node)
        for key in ("html_id", "identifier", "label"):
            value = typed_node.get(key)
            if isinstance(value, str) and value:
                ids.add(value)
        node_children = typed_node.get("children", [])
        if isinstance(node_children, list):
            stack.extend(cast(list[Any], node_children))
    return ids


def flashcard_units(data: dict[str, Any]) -> dict[str, Any]:
    units = data.get("units", {})
    if isinstance(units, dict):
        return cast(dict[str, Any], units)
    return {}


def validate_flashcard_source_href(
    card_id: str,
    href: str,
    routes: dict[str, ChapterPage],
) -> list[str]:
    errors: list[str] = []
    if "%" in href:
        errors.append(
            f"{CARD_DATA_PATH}: flashcard {card_id}: {href}: "
            f"percent-encoded chapter URLs are not allowed. {FLASHCARD_SYNC_MESSAGE}"
        )

    normalized = normalize_same_book_url(href)
    path_part, fragment = urldefrag(normalized)
    if not path_part.startswith("/chapters/"):
        errors.append(
            f"{CARD_DATA_PATH}: flashcard {card_id}: {href}: "
            f"flashcard source links must point to /chapters. {FLASHCARD_SYNC_MESSAGE}"
        )
        return errors
    if not fragment:
        errors.append(
            f"{CARD_DATA_PATH}: flashcard {card_id}: {href}: "
            f"flashcard source links must include a section fragment. {FLASHCARD_SYNC_MESSAGE}"
        )
        return errors

    target_page = routes.get(path_part.strip("/").rstrip("/"))
    if target_page is None:
        errors.append(
            f"{CARD_DATA_PATH}: flashcard {card_id}: {href}: "
            f"target chapter page does not exist. {FLASHCARD_SYNC_MESSAGE}"
        )
        return errors
    if fragment not in target_page.labels:
        errors.append(
            f"{CARD_DATA_PATH}: flashcard {card_id}: {href}: "
            f"target id #{fragment} does not match a chapter heading. "
            f"{FLASHCARD_SYNC_MESSAGE}"
        )
    return errors


def validate_flashcard_sources(routes: dict[str, ChapterPage]) -> list[str]:
    if not CARD_DATA_PATH.is_file():
        return [
            f"{CARD_DATA_PATH} does not exist. "
            "`uv run poe generate-repaso-flashcards` must run after syncing Anki."
        ]

    data = cast(dict[str, Any], json.loads(CARD_DATA_PATH.read_text(encoding="utf-8")))
    errors: list[str] = []
    for unit_key, unit_data in flashcard_units(data).items():
        if not isinstance(unit_data, dict):
            continue
        typed_unit = cast(dict[str, Any], unit_data)
        raw_cards = typed_unit.get("cards", [])
        cards: list[Any] = cast(list[Any], raw_cards) if isinstance(raw_cards, list) else []
        for card in cards:
            if not isinstance(card, dict):
                continue
            typed_card = cast(dict[str, Any], card)
            card_id = typed_card.get("id", f"unit {unit_key}")
            source_html = typed_card.get("sourceHtml", "")
            if not isinstance(source_html, str) or not source_html:
                errors.append(
                    f"{CARD_DATA_PATH}: flashcard {card_id}: missing sourceHtml. "
                    f"{FLASHCARD_SYNC_MESSAGE}"
                )
                continue
            tree = LexborHTMLParser(source_html)
            href_nodes = tree.css("a[href]")
            if not href_nodes:
                errors.append(
                    f"{CARD_DATA_PATH}: flashcard {card_id}: sourceHtml has no link. "
                    f"{FLASHCARD_SYNC_MESSAGE}"
                )
                continue
            for node in href_nodes:
                href = node.attributes.get("href", "")
                if href:
                    errors.extend(validate_flashcard_source_href(str(card_id), href, routes))
    return errors


def validate_generated_html(routes: dict[str, ChapterPage]) -> list[str]:
    errors: list[str] = []
    ids_by_file: dict[Path, set[str]] = {}
    for source_html in html_files():
        html = source_html.read_text(encoding="utf-8")
        tree = LexborHTMLParser(html)
        base_url = f"https://elc.github.io{html_route(source_html)}"
        for node in tree.css("a[href]"):
            href = node.attributes.get("href", "")
            if not href or "#" not in href:
                continue
            resolved = urlparse(urljoin(base_url, href))
            path = resolved.path.removeprefix(SAME_BOOK_BASE_PATH)
            if not path.startswith("/chapters/") or not resolved.fragment:
                continue
            if resolved.fragment in GENERATED_FRAGMENT_EXCEPTIONS:
                continue
            target_path = target_html_path(path)
            target_page = routes.get(path.strip("/").rstrip("/"))
            if not target_path.is_file():
                errors.append(f"{source_html}: {href}: target HTML file does not exist")
                continue
            if target_path not in ids_by_file:
                ids_by_file[target_path] = collect_json_ids(target_path, target_page)
            if resolved.fragment not in ids_by_file[target_path]:
                errors.append(
                    f"{source_html}: {href}: target id #{resolved.fragment} "
                    f"does not exist in {target_path}"
                )
    return errors


def check_source_links(
    pages: dict[Path, ChapterPage],
    routes: dict[str, ChapterPage],
) -> tuple[list[Path], list[str]]:
    paths = chapter_paths()
    changed: list[Path] = []
    errors: list[str] = []

    for path in paths:
        did_change, page_errors = rewrite_page_source(pages[path], routes)
        if did_change:
            changed.append(path)
        errors.extend(page_errors)
    errors.extend(validate_flashcard_sources(routes))
    return changed, errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check and fix canonical internal chapter links.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser(
        "source",
        help="Check and fix authored Markdown links and explicit targets.",
    )
    subparsers.add_parser(
        "html",
        help="Validate generated HTML/JSON href fragments after building the book.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    paths = chapter_paths()
    pages = build_pages(paths)
    routes = route_map(pages)
    changed: list[Path] = []
    errors: list[str] = []

    if args.command == "source":
        changed, errors = check_source_links(pages, routes)
    elif args.command == "html":
        errors = validate_generated_html(routes)
    else:
        raise ValueError(f"Unsupported command: {args.command}")

    if changed:
        changed_list = "\n".join(f"- {path.relative_to(REPO_ROOT)}" for path in changed)
        print(
            "Chapter links were updated. Review the changes and rerun the command:\n" + changed_list
        )
    if errors:
        print("\n".join(errors), file=sys.stderr)
    return 1 if changed or errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
