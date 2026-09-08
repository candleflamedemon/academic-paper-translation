# Academic Translation Completeness Checklist

Use this checklist after source extraction, after document assembly, and again after final rendering.

## Source inventory

- Record the PDF filename, SHA-256 hash, and page count.
- List the title, authors, affiliations, abstract, keywords, nomenclature, and every numbered and unnumbered heading.
- Record each figure number, source page, panel identifiers, and caption.
- Record each table number, row and column counts, notes, and caption.
- Record each numbered and unnumbered equation.
- Record footnotes, citations, references, data availability, funding, acknowledgements, authorship statements, conflict declarations, AI-use declarations, appendices, and supplementary-data notices.

## Translation coverage

- Map every source section to both target editions.
- Preserve all values, units, dates, percentages, signs, ranges, model names, spectral bands, metrics, and sample sizes.
- Keep citation keys and reference entries unchanged except for typography needed by the target document.
- Check terminology consistency with a short project glossary.
- Search final text for placeholders such as `TODO`, `TBD`, `待翻译`, `待补`, `缺失`, or `[[...]]`.

## Figure integrity

- Count source figures and target figures, including supplementary figures that are actually present in the supplied PDF.
- Verify every panel, outer border, axis, tick label, legend, color bar, scale bar, north arrow, annotation, and panel marker.
- Confirm that no figure contains surrounding body text or a clipped source caption.
- Confirm the embedded image aspect ratio matches its displayed aspect ratio.
- Inspect at 200% when labels are small.

## Tables and equations

- Compare every table cell, merged header, unit, decimal, dash, and note with the source.
- Confirm long tables do not lose rows across page breaks and repeat headers when needed.
- Verify equation symbols, subscripts, superscripts, fractions, summation limits, and numbering.

## Final package

- Render and inspect every page of both DOCX files.
- Confirm page count, section order, caption adjacency, and clean page breaks.
- Confirm the English original copy has the same SHA-256 hash as the source.
- Confirm all requested deliverables are in the new version directory and prior versions are untouched.

