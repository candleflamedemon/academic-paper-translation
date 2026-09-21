---
name: academic-paper-translation
description: Translate English academic papers in a user-selected fine or fast mode, create Chinese and English-Chinese DOCX editions, preserve academic content, and archive the unchanged English PDF. Use for full-paper PDF translation deliverables; do not use for short excerpts or ordinary non-academic prose.
---

# Academic Paper Translation

Produce complete academic-paper translations at the quality and speed the user chooses.

## Required preflight

Before translating, read [references/translation-modes.md](references/translation-modes.md) and perform only its lightweight preflight. Do not begin full extraction, page-by-page rendering, translation, or DOCX authoring yet.

Give the user a broad completion-time estimate for both modes in the user's language. Base it on the paper's page count and sampled complexity, the current operating system and readily available CPU/memory information, and the selected model/reasoning level when visible. If model or device details are unavailable, say so and use the typical range. Present the estimate briefly as a range, not a promise.

Then ask the user to choose:

- **A. Fine translation** - slower and higher token use, but more polished and fully checked; recommend it for core references.
- **B. Fast translation** - faster and lower token use, with plain black-and-white formatting and an adequate exploratory translation; recommend it for literature screening.
- **C. Custom** - let the user specify deliverables, formatting, or quality/latency priorities.

Do not continue until the user chooses a mode. If they select Custom, confirm only the missing requirements that materially affect the work.

## Default deliverables

Unless the user requests a different package, create:

1. `<translated-Chinese-title>_<publication-year>_中文译文版.docx`.
2. `<translated-Chinese-title>_<publication-year>_中英对照版.docx`, keeping each English unit adjacent to its Chinese translation.
3. `<translated-Chinese-title>_<publication-year>_英文原文.pdf`, as an unchanged copy of the English source PDF.

Before creating deliverables, translate the paper's displayed English title faithfully into Chinese and identify its publication year. Use `<translated-Chinese-title>_<publication-year>` as the shared folder and filename stem. Do not fall back to generic names such as `chinese.docx`, `bilingual.docx`, or `original_copy.pdf` unless the user explicitly requests them. Follow the year-selection, sanitization, shortening, and override rules in [references/local-artifact-versioning.md](references/local-artifact-versioning.md).

When local artifacts are required, read [references/local-artifact-versioning.md](references/local-artifact-versioning.md). Under a new, non-overwriting version directory in the current project's `任务成果` folder, create one `<translated-Chinese-title>_<publication-year>` folder per paper and put all of that paper's deliverables and generated reports inside it. Preserve the source and every prior version.

## Shared workflow

1. Follow the selected mode in [references/translation-modes.md](references/translation-modes.md).
2. Use the PDF skill to extract text and render source pages as required by that mode. Do not treat text extraction alone as proof of completeness.
3. Translate faithfully. Preserve numbers, units, statistical symbols, sample sizes, uncertainty, qualifications, in-text citations, and reference entries. Keep recurring technical terms and abbreviations consistent.
4. Reconstruct the two Word editions with the documents skill. Keep figure and table captions adjacent to their objects, and use native Word tables and equations where practical.
5. Preserve every figure without changing its aspect ratio. Prefer direct embedded-image extraction; for vectors or multi-object figures, render and crop the complete figure with a safety margin rather than using thumbnails or contact sheets.
6. Render both final DOCX files to page images and inspect every page. Fine mode includes content and visual-polish iteration; fast mode limits iteration to missing content, clipping, overlap, distorted images, unreadable glyphs, and other defects that block reliable reading.
7. Run `scripts/verify_translation_package.py` with the counts collected for the selected mode. Hash-check the archived English PDF against the source. Script results supplement, but do not replace, visual inspection.

## Shared acceptance criteria

- All tables, equations, captions, citations, references, and end matter are present.
- Chinese and bilingual editions contain the same substantive content.
- The archived English PDF is byte-identical to the supplied source.
- Default deliverable filenames share the sanitized Chinese title translation and publication year, use the correct edition suffix, and sit together in the matching paper folder; user-specified naming takes precedence.
- Final DOCX renders have no visible defects.
- Fine mode additionally meets the one-to-one coverage and publication-ready criteria in [references/completeness-checklist.md](references/completeness-checklist.md).
- Fast mode remains a plain exploratory edition: it must be complete and readable, but it need not reproduce the journal's visual design or receive a separate stylistic-polish pass.
