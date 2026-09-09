# Translation Modes and Time Estimate

Use this reference before translation to estimate duration and obtain the user's mode choice, then follow only the selected mode.

## Lightweight preflight

Keep preflight brief. Do not fully translate, render every page, or build the final documents during this step.

1. Read the PDF page count and metadata. Sample the title, abstract, one middle section, and the final pages; inspect one or two additional pages only when the sampled content is not representative.
2. Classify complexity:
   - **Light:** born-digital, mostly prose, reliable extraction, few figures/tables/equations.
   - **Mixed:** two-column or dense layout, regular figures/tables/equations, or some extraction cleanup.
   - **Heavy:** scanned/OCR-dependent pages, poor extraction, many complex tables/equations, dense multi-panel figures, or unusual scripts/fonts.
3. Read only readily available system facts: operating system, logical CPU count, and total or available memory. Do not benchmark, install software, or run a full-document conversion for the estimate.
4. Use the selected model and reasoning level if they are visible. Never switch models merely to estimate. If this information is hidden, label it unknown and use the typical adjustment.

## Rough estimate

Use the page count and these broad baseline ranges:

| Complexity | Fast mode | Fine mode |
| --- | ---: | ---: |
| Light | 1-2 min/page + 5-15 min | 3-6 min/page + 15-30 min |
| Mixed | 2-4 min/page + 5-15 min | 6-12 min/page + 15-30 min |
| Heavy | 4-7 min/page + 5-15 min | 12-20 min/page + 15-30 min |

Adjust once, approximately:

- Constrained device or difficult local rendering/OCR: add about 25%.
- Strong device with reliable extraction/rendering: subtract at most 15%.
- Speed-oriented model/reasoning: subtract at most 15%.
- Deliberative or highest-quality model/reasoning: add about 20%.

Round outward to convenient 10-minute or half-hour boundaries. Use a wider range when details are unknown. Keep the user-facing estimate to a few lines: page count, complexity, relevant environment/model note, and estimated time for both modes. State that network load, OCR quality, and layout repairs can change the result.

## Fine translation

Use for core references and publication-ready reading copies.

1. Read [completeness-checklist.md](completeness-checklist.md) and build the full source inventory and one-to-one coverage ledger.
2. Translate section by section, maintain a short terminology glossary, and perform a separate consistency and language-polish pass.
3. Reconstruct readable, professionally typeset Chinese and bilingual editions. Preserve complete figures, panels, tables, equations, captions, footnotes, references, declarations, appendices, and supplementary notices.
4. Render and inspect every final DOCX page at full size. Iterate for both content fidelity and visual polish until the fine-mode acceptance criteria pass.

## Fast translation

Use for exploratory reading and literature screening.

1. Build a lightweight coverage ledger containing source page count, section order, and counts of figures, tables, and equations, plus the presence of references and end matter.
2. Translate each section once in reasonably sized batches. Keep terminology consistent and repair clear meaning errors, but do not run a separate stylistic rewriting pass.
3. Use a simple black-and-white, single-column Word layout with standard title, heading, body, caption, table, and equation styles. Do not imitate the journal layout or add decorative colors, cover art, text boxes, or nonessential headers/footers.
4. Preserve all substantive content in source order. Use simple native Word tables and equations where practical; preserve complete figures at a readable size without elaborate layout reconstruction.
5. Render and inspect every final DOCX page once. Iterate only when content is missing or unreadable, or when clipping, overlap, distorted images, broken tables, missing glyphs, or bad page breaks prevent reliable reading.

Fast mode reduces translation and layout refinement; it does not authorize omissions. Describe its output as an exploratory translation rather than publication-ready work.
