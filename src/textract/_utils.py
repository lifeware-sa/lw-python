from textractor.parsers import response_parser

def textract_json_result_to_md(textract_json_result) -> str:
    textracted = response_parser.parse(textract_json_result)
    return textracted.to_markdown()