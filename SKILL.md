---
name: academic-paper-translation
description: Translate English academic papers into complete Chinese and English-Chinese bilingual editions, preserve figures, tables, equations, citations, and archive the unchanged English original. Use for PDF-to-DOCX academic translation deliverables; do not use for short excerpts or ordinary non-academic prose.
---

# Academic Paper Translation

Produce publication-ready academic translations without losing source content or visual information.

## Default deliverables

Unless the user requests a different package, create:

1. A Chinese-only `.docx`.
2. An English-Chinese bilingual `.docx`, keeping each English unit adjacent to its Chinese translation.
3. An unchanged copy of the English source PDF.

When local artifacts are required, use `$save-task-artifacts` and place all deliverables in one new, non-overwriting version directory. Preserve the source and every prior version.

## Workflow

1. Use the PDF skill to extract text and render every source page. Build a source inventory before translating: page count, headings, figures, tables, equations, captions, footnotes, references, acknowledgements, declarations, appendices, and supplementary-data notices.
2. Read [references/completeness-checklist.md](references/completeness-checklist.md) and maintain a one-to-one coverage ledger. Do not treat text extraction alone as proof of completeness.
3. Translate faithfully. Preserve numbers, units, statistical symbols, sample sizes, uncertainty, qualifications, in-text citations, and reference entries. Standardize recurring technical terms and abbreviations; on first occurrence, give the Chinese term followed by the English name or abbreviation when helpful.
4. Reconstruct the two Word editions with the documents skill. Use native Word tables and equations where practical. Keep figure and table captions adjacent to their objects.
5. For every figure, prefer direct embedded-image extraction. If the figure is composed of PDF vectors or multiple objects, render the source page at 300 DPI or higher and crop the complete figure bounding box with a safety margin. Include every panel, axis, tick label, legend, scale bar, compass, border, and panel identifier. Never crop from thumbnails or contact sheets, and never stretch a figure to a different aspect ratio; pad with whitespace or adjust the layout instead.
6. Render both final DOCX files to page images. Inspect every page at full size, with special attention to figures, long tables, equations, page breaks, captions, and glyphs. Iterate until no clipping, overlap, missing content, or distorted image remains.
7. Run `scripts/verify_translation_package.py` with expected counts from the coverage ledger. Hash-check the archived English PDF against the source. A successful script result supplements, but does not replace, visual inspection.

## Acceptance criteria

- Source inventory and translated content match one-to-one.
- All figures and panels are readable and uncropped.
- All tables, equations, captions, citations, references, and end matter are present.
- Chinese and bilingual editions contain the same substantive content.
- The archived English PDF is byte-identical to the supplied source.
- Final DOCX renders have no visible defects.
