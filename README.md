# lw-python
The python code of Lifeware

## Build Tools

This project uses [**uv**](https://docs.astral.sh/uv/) for Python package management and [**just**](https://github.com/casey/just) as a command runner. These tools provide a streamlined development experience:

- **uv**: A fast, reliable Python package installer and resolver
- **just**: A handy way to save and run project-specific commands (similar to Make, but simpler)

Run `just --list` to see all available commands.

## Setup

### Prerequisites

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and [just](https://github.com/casey/just#installation).

On Windows, if the packaged executable fails with an error such as `Error loading Python DLL`, install the **Microsoft Visual C++ Redistributable (2015-2022)**:

```bash
winget install Microsoft.VCRedist.2015+.x64
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

With the packaged executable (built by `just build` into `dist/main/`):
```bash
./main textract-to-md --from <input.json> --to <output.md>
```

**Options:**
- `-f, --from <path>`: Input UTF-8 JSON file containing a raw AWS Textract response (`DetectDocumentText` or `AnalyzeDocument`). Must exist.
- `-t, --to <path>`: Output Markdown file path (written as UTF-8 with LF line endings on every OS).

Both options are needed for the conversion, but they are not enforced by the CLI: if either is missing, or the conversion fails, the command prints `An error occurred: <message>` to stdout and still exits with code `0`. Callers should check the output for that message (or check that the output file was created) to detect failures.
