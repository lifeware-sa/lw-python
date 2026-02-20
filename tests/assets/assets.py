from pathlib import Path
import json

assets_path = Path(__file__).parent

textract_analyze_result_path = assets_path / 'textract_analyze_result.json'
textract_detect_result_path = assets_path / 'textract_detect_result.json'
pdf_test_file_path = assets_path / 'test_pdf_to_md.pdf'
docx_test_file_path = assets_path / 'test_docx_to_md.docx'

def _get_docx_path() -> str:
    return str(docx_test_file_path)

def _get_pdf_path() -> str:
    return str(pdf_test_file_path)

def _get_json_content(path: Path | str):
    with open(path, 'r') as input:
        return json.load(input)
    

def pdf_file_path():
    return _get_pdf_path()
def docx_file_path():
    return _get_docx_path()
def textract_analyze_result():
    return _get_json_content(textract_analyze_result_path)
def textract_detect_result():
    return _get_json_content(textract_detect_result_path)