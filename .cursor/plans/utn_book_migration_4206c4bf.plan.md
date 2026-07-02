---
name: UTN Book Migration
overview: Convert `D:\repositories\utn-artificial-intelligence\units` into a MyST/Jupyter Book project modeled on `probabilidad/book`, preserving theory content as-is while making the Prolog practice material runnable with collapsed solutions.
todos:
  - id: audit-source
    content: Inventory canonical `units/` files and confirm there are no duplicate/generated source trees to migrate.
    status: pending
  - id: bootstrap-book
    content: Add a slim MyST/Jupyter Book scaffold modeled on `probabilidad` and the template repo.
    status: pending
  - id: migrate-chapters
    content: Copy theory markdown and images into `book/chapters/` with stable ASCII slugs while preserving visible content.
    status: pending
  - id: configure-toc
    content: Create `book/myst.yml` metadata, navigation, and nested unit/practice/exam TOC.
    status: pending
  - id: prolog-spike
    content: Validate `calysto_prolog` install, kernelspec registration, MyST code-cell execution, and Binder compatibility.
    status: pending
  - id: prolog-conversion
    content: Convert Unit 6 practice exercises into runnable Prolog pages with collapsed solutions.
    status: pending
  - id: ci-binder
    content: Add Poe tasks, CI Pages workflows, and Binder setup with kernel installation.
    status: pending
  - id: validate-build
    content: Run book build/preview checks and fix Markdown, image, anchor, or kernel failures.
    status: pending
isProject: false
---

# UTN AI Jupyter Book Migration Plan

## Target Shape

Create a new Jupyter Book 2/MyST structure inside `D:\repositories\utn-artificial-intelligence`, borrowing the proven layout from `D:\repositories\probabilidad` while keeping the UTN content organized by unit. The project identity should be `classic-ai`, with references adapted consistently across config, package metadata, Binder, Docker tags, CI, and site metadata. The visible book title should be `Inteligencia Artificial Clásica`. The GitHub target is `https://github.com/ELC/classic-ai`. Theory content should be deployed faithfully: no pedagogical rewrite, no content tuning, and no cleanup that changes what students see. Long theory files may be split into multiple pages when the split follows the original semantic structure.

Do not rename the local folder during this migration; it may remain `D:\repositories\utn-artificial-intelligence` even though project/repo identity is `classic-ai`.

Assume git/remote setup is handled outside this plan. Do not initialize git or create commits as part of the migration unless explicitly requested later.

Proposed structure:

```text
D:\repositories\utn-artificial-intelligence\
  book\
    myst.yml
    chapters\
      welcome.md
      unit-01-introduccion\unit-01.md
      unit-01-introduccion\exam-preparation.md
      unit-02-busqueda-y-planificacion\*.md
      unit-02-busqueda-y-planificacion\exam-preparation.md
      unit-03-representacion-conocimiento\*.md
      unit-03-representacion-conocimiento\exam-preparation.md
      unit-04-ingenieria-conocimiento\unit-04.md
      unit-04-ingenieria-conocimiento\exam-preparation.md
      unit-05-redes-neuronales\unit-05.md
      unit-05-redes-neuronales\exam-preparation.md
      unit-06-prolog\unit-06.md
      unit-06-prolog\practica-01.md      # one converted page per original practice sheet
      unit-06-prolog\practica-02.md
      unit-06-prolog\practica-03.md
      unit-06-prolog\practica-04.md
      unit-06-prolog\exams\...        # static appendix in first pass
    assets\
    bibliography.bib
  pyproject.toml
  .python-version
  .binder\Dockerfile
  .github\workflows\ci.yml
  .github\workflows\pages.yml
```

Use MyST Markdown (`.md`) for all migrated pages, including executable Prolog practice pages. Keep each unit as a folder under `book/chapters/` so existing unit-local image references like `images/foo.png` continue to work with minimal edits. Use `book/assets/` only for site-level assets such as logos and favicon. Normalize URL slugs to ASCII Spanish names (`introduccion`, `planificacion`, etc.) instead of preserving the current `introducci6n` filenames. Use `welcome.md` as the single book landing page; do not create per-unit `index.md` landing pages.

Content policy:

- Units 1-5 theory and any other theory pages are a faithful publication pass. Only add the minimum wrapper needed for MyST/Jupyter Book: frontmatter, TOC registration, path changes, and build-only escaping if absolutely required.
- For code-like examples in theory pages, add fenced code blocks only when needed to preserve original visual formatting or prevent Markdown wrapping from damaging the example. Do not systematically refactor all theory examples into executable or syntax-highlighted blocks.
- Structured citation conversion is allowed: extract visible source references into `book/bibliography.bib` and replace those reference mentions with MyST citations where appropriate, without rewriting the surrounding theory text. When a reference lacks complete metadata, create a best-effort BibTeX entry with an explicit TODO/comment for later verification.
- Reasonable semantic splitting is allowed for long theory pages. Split only at existing meaningful boundaries such as original `CAPITULO`, major `##` sections, or clearly self-contained topics. Preserve the original text, order, headings, examples, and images inside each split.
- Do not remove pasted PDF indices, rewrite headings, restructure explanations, convert prose, or apply the `probabilidad` pedagogical pattern to the theory content.
- `unit-06-prolog/unit-06.md` is still treated as theory/reference content and should be preserved like the other theory pages.
- Unit 6 practice and exam material is intentionally different: exercises should become runnable Prolog activities, with solutions hidden by default so students can try first. For practice pages, preserve the original prompt wording and order, but allow structural wrapping with headings, runnable cells, verification queries/tests, and dropdown solutions.
- A separate chapter with an embedded Prolog interpreter independent of MyBinder is explicitly out of scope for this migration and should be planned later.
- After migration, `book/chapters/` becomes the maintained book source. Keep `units/` as archived original material; do not delete it and do not build the book from it dynamically.
- `welcome.md` should be a minimal course index: visible title, short description, unit list, Binder launch link, and a note that theory content is preserved from the original material.
- Publish the book content under CC BY-NC-SA 4.0 International, with clear source/UTN attribution in site metadata and the welcome page.
- In `book/myst.yml`, list Ezequiel Leonardo Castaño as maintainer/adapter; keep original UTN/source attribution in the welcome and license text.

## Implementation Plan

1. Bootstrap the book infrastructure from `D:\repositories\jupyter-book-template` / `D:\repositories\probabilidad`.

   Add `book/myst.yml`, `pyproject.toml`, `.python-version`, `.binder/`, `.github/workflows/`, `.gitignore`, and minimal assets. Use `classic-ai` for the Python project name, Docker image tag, Binder references, Pages `BASE_URL`, and any generated site/project identifiers. Use `Inteligencia Artificial Clásica` as `project.title` and `https://github.com/ELC/classic-ai` as `project.github`. Copy the Ethical Ads plugin/banner from `probabilidad` and update its book title/configuration for `Inteligencia Artificial Clásica`. Start slim: `jupyter-book`, `jupyterlab`, `poethepoet`, `prek`, `ruff`, `metakernel`, and `calysto_prolog`. Pin `.python-version` to the newest Python version that works reliably with the chosen MetaKernel Prolog stack, even if that differs from the Python 3.13 used by `probabilidad`. Defer the heavy `src/`/tests architecture from `probabilidad` unless the course later needs reusable Python libraries.

   Add license metadata/docs for CC BY-NC-SA 4.0 International.

2. Configure `book/myst.yml` to mirror `probabilidad/book/myst.yml`.

   Use `project.title`, `authors`, `github`, `numbering.headings: true`, `site.template: book-theme`, `site.options.folders: true`, the Ethical Ads plugin/banner, the existing Google Analytics measurement ID from `probabilidad`, and a nested `toc`.

   The TOC should group each academic unit as a title-only section with its content pages as children. Include Units 1-5 `exam_preparation.md` files as child study-guide pages, preserving their content as-is. Unit 6 should get interactive practice pages first, plus a mostly static exam bank appendix rather than flattening all 30 exams into the top level.

3. Migrate theory content from `units/` only, preserving visible content.

   Treat `D:\repositories\utn-artificial-intelligence\units` as canonical. First confirm the current repo has no duplicate/generated source trees that need cleanup. Copy or split each `unit-XX.md` under `book/chapters/<unit-slug>/`, copy each `exam_preparation.md` to `exam-preparation.md`, and copy unit-local `images/` folders unchanged. Do not create unit-level `index.md` files.

   Add MyST frontmatter to every chapter. For static theory pages, use only `title` and optional `short_title`. Do not add kernelspecs to non-executable theory pages. Keep original visible Markdown content intact even when it contains OCR artifacts, pasted indices, raw code-like text, or uneven formatting.

   After this migration, make future book edits in `book/chapters/`. Preserve `units/` as the original source archive rather than generating `book/chapters/` from it on every build.

   Suggested split policy:

   - Keep short units as a single unit page when navigation is already manageable.
   - Split theory units over about 1,500 lines automatically at existing `##` headings. Based on the current corpus, this likely affects Units 1, 2, and 3.
   - Name generated split pages with sequence-prefixed heading slugs, for example `01-espacio-busqueda.md`, to preserve reading order and keep URLs readable.
   - When a split unit has content before the first `##`, merge that preface material into the first generated section page.
   - Rewrite internal links affected by splitting and add stable MyST labels where needed instead of relying only on generated heading anchors.
   - Temporary migration scripts may be used to split pages and rewrite links, but remove those scripts before finalizing unless explicitly requested otherwise.
   - Use title-only unit groups in `book/myst.yml` and register the unit pages as children.
   - Add previous/next context through the TOC, not by rewriting the source content.

4. Make only build-preserving fixes to theory pages.

   If MyST fails to parse a theory page, fix the smallest technical issue possible while preserving the rendered content. Prefer local escaping, protective fenced blocks, raw text blocks, or MyST-safe wrapping over editorial cleanup. Do not remove PDF page-number TOCs, repair wording, normalize prose, or convert raw examples to new teaching formats unless the page cannot build otherwise.

5. Validate Calysto Prolog before making Prolog pages executable.

   Use Calysto Prolog as the preferred kernel because it is MetaKernel-based, but run a short spike first. It is old (`0.8.4`) and has known issue reports, so the build should not depend on all Prolog content executing until the smoke test passes.

   Add a temporary or early `unit-06-prolog/kernel-smoke.md` page with frontmatter like:

   ```yaml
   ---
   title: Prolog Kernel Smoke Test
   kernelspec:
     name: calysto_prolog
     display_name: Calysto Prolog
   ---
   ```

   Then test the exact MyST code-cell syntax, Calysto query syntax, and whether the chosen MetaKernel backend supports SWI-Prolog-compatible PlUnit tests. Calysto examples use queries like `child(NAME)?`, so UTN examples written as `?- consulta.` may need either static display or syntax adaptation for executable cells. MetaKernel support has priority over PlUnit: use PlUnit if it works in the MetaKernel path; otherwise provide runnable verification queries compatible with the selected kernel.

6. Wire kernel installation into local, CI, and Binder builds.

   Add a Poe task such as `install-kernels` that runs `python -m calysto_prolog install --user`, and make `build-book` depend on it when executable Prolog pages are enabled. In `.binder/Dockerfile`, run the same kernelspec install after `uv sync`, then verify Binder exposes `calysto_prolog` in JupyterLab.

   If Calysto fails on Python 3.13/JupyterLab 4.5, the first migration is blocked until a MetaKernel-compatible path is chosen: pin a compatible Python/Jupyter stack, patch/fork Calysto, or adopt another MetaKernel-based Prolog kernel. Static Prolog rendering alone is not enough to complete the first migration.

   Binder support is a release gate for the first migration. The migration is not complete until the hosted Binder environment starts and exposes the selected MetaKernel Prolog kernel for students.

7. Convert Unit 6 practice into runnable exercises with collapsed solutions.

   Preserve `unit-06-prolog/unit-06.md` as a faithful theory/reference page. Treat `practica-01.md` through `practica-04.md` as the first interactive conversion scope, keeping one page per original practice sheet. Each practice exercise should have:

   - The original exercise prompt visible to students, preserving wording and order.
   - Inline runnable Prolog code blocks/cells after the Calysto smoke test passes.
   - Manual sample queries students can run.
   - PlUnit tests students can run to verify their solution when supported by the MetaKernel backend.
   - Runnable verification queries as the fallback when PlUnit is not supported.
   - A collapsed solution block, for example with MyST dropdown syntax, so students can try the exercise before seeing the answer.
   - Any required data included inline when practical; external files are reserved for the later exam-bank pass.
   - Execution tags that prevent incomplete student starter cells from running during the book build.

   Practice pages should be self-contained MyST files. Do not create or depend on separate `.pl` files for `practica-01.md` through `practica-04.md`; existing practice `.pl` files outside `units/` may be used as source material, but their contents should be embedded into the MyST pages as code cells or fenced code blocks.

   The conversion may add headings, cells, tests, and dropdown blocks around each exercise, but should not rewrite the exercise prompt into a new pedagogical voice.

   Build execution policy: CI should execute only solution and verification cells that are expected to pass. Student starter cells should be present and runnable interactively, but tagged so they do not execute during `uv run poe build-book`.

   Keep existing exam `solution.pl` files for the later exam conversion pass. For TODO/stub exam solutions, either omit the collapsed solution from the first pass or mark it clearly as pending rather than presenting it as a solved answer.

   Example solution wrapper:

   ```md
   :::{dropdown} Solución
   ```prolog
   % solution.pl content here
   ```
   :::
   ```

   The exam bank should be included as an appendix-like static section in the first pass. Execution should be enabled exercise-by-exercise only in a later pass when each solution and fixture set has been verified.

8. Add quality gates.

   Keep `cspell.json` and its Spanish dictionary. Add build validation with `uv run poe build-book`, local preview with `uv run poe serve-book`, and CI/Page deployment using the same `BASE_URL=/<repo-name>` pattern as `probabilidad`. Add Python/uv-managed Markdown linting/formatting for `book/chapters/`, preferably with `mdformat`, that wraps prose at 80 characters. Also include basic formatting/linting for config and scripts. Treat Markdown wrapping as source formatting only: it must not change rendered theory content. Do not reformat archived `units/` files. Add a Binder Docker build check because Binder support is a release gate. Add a lightweight link/image sanity check if missing image references appear during the migration.

   Add a bibliography validation pass as references are converted into `book/bibliography.bib`, and enable numbered references in `book/myst.yml` following the `probabilidad` pattern.

9. Defer the standalone embedded Prolog interpreter.

   Do not include a browser-embedded interpreter independent of MyBinder in this migration, and do not create a placeholder chapter for it. Capture it only as future work in the plan and, if useful, in a concise future-work note in project documentation after the book deploys and the Calysto/Jupyter execution path is understood. That future plan can compare options such as SWI-Prolog compiled to WebAssembly, Tau Prolog, Pengines, or a custom frontend widget.

## Key Risks

- Calysto Prolog may not work cleanly with the modern Python/Jupyter stack or may not support SWI-Prolog PlUnit; isolate that risk with the kernel smoke test and keep MetaKernel compatibility as the priority. Because Binder is a release gate, kernel issues must be resolved before calling the migration complete, including pinning Python to the newest compatible version if needed.
- Units over about 1,500 lines, likely Units 1, 2, and 3, should be split automatically at existing `##` headings while preserving content and order.
- Existing Markdown has OCR/PDF artifacts, malformed tables, and raw code; preserve them in theory pages unless they break the build.
- Citation conversion touches theory pages; keep changes limited to converting explicit references into MyST citations and avoid prose rewrites.
- The Unit 6 exam bank is large and uneven; include it as an appendix-like static section first and defer runnable exam conversion.
- Internal links in `exam_preparation.md` depend on heading slugs; rewrite them during splitting and add explicit MyST labels rather than relying only on auto-generated anchors.
- The standalone embedded Prolog interpreter has different technical constraints from Jupyter/Binder execution and should not be mixed into this first migration.
- Maintaining both `units/` and `book/chapters/` creates duplication; document that `book/chapters/` is authoritative after migration.

## Acceptance Criteria

- `uv sync --all-groups` completes from `D:\repositories\utn-artificial-intelligence`.
- `uv run poe build-book` produces `book/_build/html` successfully.
- Markdown linting/formatting wraps `book/chapters/` source text at 80 characters without changing rendered theory content; archived `units/` files remain untouched.
- The generated site has a unit-based sidebar similar to `probabilidad/book`.
- Theory pages preserve the original visible content, including existing wording, ordering, indices, examples, and formatting quirks except for unavoidable build-safe wrapping.
- Visible source references are converted to structured MyST citations backed by `book/bibliography.bib` without rewriting surrounding theory prose.
- Long theory units may be split into semantic child pages using existing `##` headings, and those splits preserve the original section sequence.
- `book/chapters/` is documented as the maintained book source after migration, while `units/` remains as archived original material.
- Existing images render from their migrated chapter folders.
- `unit-06-prolog/unit-06.md` preserves the original visible theory/reference content.
- Unit 6 practice exercises (`practica-01.md` through `practica-04.md`) are self-contained MyST pages with inline runnable code, manual sample queries, PlUnit tests when supported, fallback verification queries when needed, and complete solutions hidden in collapsed blocks by default.
- CI executes only Unit 6 solution/verification cells that are expected to pass; incomplete starter cells are skipped during build but runnable interactively.
- The Unit 6 exam bank is present as static appendix content in the first pass, not fully interactive.
- Binder starts JupyterLab and shows the selected MetaKernel Prolog kernel as part of the first migration acceptance criteria.
- The independent embedded Prolog interpreter is documented as deferred, not implemented in this migration.