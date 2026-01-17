# SplitPDF

A tiny CLI tool for breaking long study PDFs into bite-sized, fixed-length chunks so reviewing and annotating become manageable.

I like using this to study with the help of LLMs. 
You can break down a pdf into bite sized chunks and let the LLM ask you questions about it.

## Getting Started

1. Install dependencies with `uv` (requires Python 3.13+):
   ```sh
   uv sync
   ```
2. Run the script directly:
   ```sh
   python split_pdf.py path/to/your.pdf
   ```
3. Or use the console entry point through `uv run`:
   ```sh
   uv run splitpdf path/to/your.pdf --pages 12
   ```

Each invocation creates `{original}_partN.pdf` files in the same folder, reporting the page ranges for every chunk.
