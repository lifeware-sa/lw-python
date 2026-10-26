# lw-python
The python code of Lifeware

## Build Tools

This project uses [**uv**](https://docs.astral.sh/uv/) for Python and package management.

## Setup

### Prerequisites

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

On Windows, if the packaged executable fails with an error such as `Error loading Python DLL`, install the **Microsoft Visual C++ Redistributable (2015-2022)**:

```bash
winget install Microsoft.VCRedist.2015+.x64
```

### Installation

Set up the project:
```bash
uv sync --all-groups
```

This installs the Python version from `.python-version` (if needed), creates the `.venv` virtual environment, and installs all dependencies.

### Common commands

```bash
uv run pytest -vv                                   # run the tests
uv run pyinstaller --noconfirm --clean main.spec    # build the executable into dist/main/
uv lock --check                                     # check that uv.lock is up to date
```

## CLI Commands

The project provides the following Click commands:

### textract-to-md
Converts AWS Textract JSON output to Markdown format.

**Usage:**
```bash
python -m lwPython.main textract-to-md --from <input.json> --to <output.md>
```

With the packaged executable (built into `dist/main/`):
```bash
./main textract-to-md --from <input.json> --to <output.md>
```

**Options:**
- `-f, --from <path>`: Input UTF-8 JSON file containing a raw AWS Textract response (`DetectDocumentText` or `AnalyzeDocument`). Must exist.
- `-t, --to <path>`: Output Markdown file path (written as UTF-8 with LF line endings on every OS).

Both options are needed for the conversion, but they are not enforced by the CLI: if either is missing, or the conversion fails, the command prints `An error occurred: <message>` to stdout and still exits with code `0`. Callers should check the output for that message (or check that the output file was created) to detect failures.
