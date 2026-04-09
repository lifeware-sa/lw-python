def save_markdown(content: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def textract_json_result_to_md(textract_json_result) -> str:
    from textractor.parsers import response_parser
    textracted = response_parser.parse(textract_json_result)
    return textracted.to_markdown()