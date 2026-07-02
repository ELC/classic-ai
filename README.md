# Inteligencia Artificial Clásica

Libro digital construido con Jupyter Book 2 y MyST para publicar material
clásico de Inteligencia Artificial.

Sitio previsto: https://elc.github.io/classic-ai/

## Desarrollo local

```bash
uv sync --all-groups
uv run poe build-book
uv run poe serve-book
uv run poe ci
```

## Binder local

```bash
uv run poe build-docker
docker run --rm -p 8888:8888 classic-ai:binder
```

El contenido bajo `book/chapters/` es la fuente mantenida del libro.
