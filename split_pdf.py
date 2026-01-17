#!/usr/bin/env python3
"""Split a PDF file into chunks of 10 pages each."""

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def split_pdf(input_path: Path, pages_per_chunk: int = 10) -> list[Path]:
    """Split a PDF into multiple files with specified pages per chunk."""
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    if total_pages == 0:
        print(f"Error: {input_path} has no pages")
        sys.exit(1)

    output_files = []
    stem = input_path.stem
    parent = input_path.parent

    for start in range(0, total_pages, pages_per_chunk):
        end = min(start + pages_per_chunk, total_pages)
        chunk_num = (start // pages_per_chunk) + 1

        writer = PdfWriter()
        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_path = parent / f"{stem}_part{chunk_num}.pdf"
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        output_files.append(output_path)
        print(f"Created: {output_path} (pages {start + 1}-{end})")

    return output_files


def main():
    parser = argparse.ArgumentParser(description="Split a PDF into 10-page chunks")
    parser.add_argument("pdf_file", type=Path, help="Path to the PDF file to split")
    parser.add_argument(
        "-n", "--pages",
        type=int,
        default=10,
        help="Number of pages per chunk (default: 10)"
    )
    args = parser.parse_args()

    if not args.pdf_file.exists():
        print(f"Error: File not found: {args.pdf_file}")
        sys.exit(1)

    if not args.pdf_file.suffix.lower() == ".pdf":
        print(f"Error: File must be a PDF: {args.pdf_file}")
        sys.exit(1)

    print(f"Splitting {args.pdf_file} into {args.pages}-page chunks...")
    output_files = split_pdf(args.pdf_file, args.pages)
    print(f"\nDone! Created {len(output_files)} file(s)")


if __name__ == "__main__":
    main()
