import os
from contextlib import contextmanager

@contextmanager
def _unix_linesep():
    # textractor mixes hardcoded "\n" with os.linesep (as separator and when merging lines),
    # so on Windows ("\r\n") both line endings and layout differ from Linux/macOS.
    # It reads os.linesep both at import time and while converting, so the import and the
    # conversion must both happen inside this context.
    original = os.linesep
    os.linesep = "\n"
    try:
        yield
    finally:
        os.linesep = original

def save_markdown(content: str, output_path: str):
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

def textract_json_result_to_md(textract_json_result) -> str:
    with _unix_linesep():
        from textractor.parsers import response_parser
        textracted = response_parser.parse(textract_json_result)
        return textracted.to_markdown()
