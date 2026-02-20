import os

from textractor.parsers import response_parser

def sanitize_string(string) -> str:
    if os.name == "nt":
        return string.replace("\r\n", "\n")
    return string

def textract_json_result_to_md(textract_json_result) -> str:
    textracted = response_parser.parse(textract_json_result)
    return sanitize_string(textracted.to_markdown())