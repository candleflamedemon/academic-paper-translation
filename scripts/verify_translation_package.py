#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

from pypdf import PdfReader


PLACEHOLDERS = re.compile(r"TODO|TBD|待翻译|待补|缺失|\[\[[^\]]+\]\]", re.I)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inspect_docx(path: Path) -> dict:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        document = archive.read("word/document.xml").decode("utf-8", "replace")
    images = [name for name in names if name.startswith("word/media/") and not name.endswith("/")]
    return {
        "path": str(path),
        "images": len(images),
        "tables": document.count("<w:tbl>"),
        "equations": len(re.findall(r"<m:oMath(?:\s|>)", document)),
        "placeholder_hits": sorted(set(PLACEHOLDERS.findall(document))),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify an academic-paper translation package.")
    parser.add_argument("--source-pdf", type=Path, required=True)
    parser.add_argument("--original-copy", type=Path, required=True)
    parser.add_argument("--docx", type=Path, action="append", required=True)
    parser.add_argument("--expected-pdf-pages", type=int)
    parser.add_argument("--expected-images", type=int)
    parser.add_argument("--expected-tables", type=int)
    parser.add_argument("--expected-equations", type=int)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    source_pages = len(PdfReader(str(args.source_pdf)).pages)
    source_hash = sha256(args.source_pdf)
    copy_hash = sha256(args.original_copy)
    report = {
        "source_pdf": str(args.source_pdf),
        "source_pages": source_pages,
        "source_sha256": source_hash,
        "original_copy_sha256": copy_hash,
        "original_copy_matches": source_hash == copy_hash,
        "documents": [inspect_docx(path) for path in args.docx],
        "errors": [],
    }

    if not report["original_copy_matches"]:
        report["errors"].append("The archived English PDF is not byte-identical to the source.")
    if args.expected_pdf_pages is not None and source_pages != args.expected_pdf_pages:
        report["errors"].append(f"Expected {args.expected_pdf_pages} PDF pages, found {source_pages}.")
    for item in report["documents"]:
        for key, expected in (
            ("images", args.expected_images),
            ("tables", args.expected_tables),
            ("equations", args.expected_equations),
        ):
            if expected is not None and item[key] != expected:
                report["errors"].append(f"{item['path']}: expected {expected} {key}, found {item[key]}.")
        if item["placeholder_hits"]:
            report["errors"].append(f"{item['path']}: placeholder text found: {item['placeholder_hits']}")

    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.report:
        args.report.write_text(rendered + "\n", encoding="utf-8")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
