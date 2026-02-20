# lw-python
The python code of Lifeware

## Build Tools

This project uses [**uv**](https://docs.astral.sh/uv/) for Python package management and [**just**](https://github.com/casey/just) as a command runner. These tools provide a streamlined development experience:

- **uv**: A fast, reliable Python package installer and resolver
- **just**: A handy way to save and run project-specific commands (similar to Make, but simpler)

Run `just --list` to see all available commands.

## Setup

### Prerequisites

Install the required system dependencies:

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use:
```bash
choco install ffmpeg
```

### Installation

Run the setup command to configure the project:
```bash
just setup
```

This will install Python, create a virtual environment, and sync all dependencies.

## CLI Commands

The project provides the following Click commands:

### textract-to-md
Converts AWS Textract JSON output to Markdown format.

**Usage:**
```bash
python -m lwPython.main textract-to-md --from <input.json> --to <output.md>
```

**Options:**
- `-f, --from <path>`: Input JSON file from AWS Textract (required)
- `-t, --to <path>`: Output Markdown file path (required)

### docling-pdf-to-md
Converts a PDF to Markdown using Docling.

**Usage:**
```bash
python -m lwPython.main docling-pdf-to-md --from <input.pdf> --to <output.md>
```

**Options:**
- `-f, --from <path>`: Input PDF file (required)
- `-t, --to <path>`: Output Markdown file path (required)

### markitdown-file-to-md
Converts a PDF or DOCX file to Markdown using MarkItDown.

**Usage:**
```bash
python -m lwPython.main markitdown-file-to-md --from <input.pdf|input.docx> --to <output.md>
```

**Options:**
- `-f, --from <path>`: Input PDF or DOCX file (required)
- `-t, --to <path>`: Output Markdown file path (required)