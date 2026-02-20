from pathlib import Path

expecteds_path = Path(__file__).parent

textract_analyze_result_path = expecteds_path / 'expected_textract_analyze_result.md'
textract_detect_result_path = expecteds_path / 'expected_textract_detect_result.md'
docling_result_path = expecteds_path / 'expected_docling.md'
markitdown_pdf_result_path = expecteds_path / 'expected_pdf_markitdown.md'
markitdown_docx_result_path = expecteds_path / 'expected_docx_markitdown.md'

def _get_raw_content(path: Path | str):
    with open(path, 'r') as input:
        return input.read()

def markitdown_pdf_expected():
    return _get_raw_content(markitdown_pdf_result_path)
def markitdown_docx_expected():
    return _get_raw_content(markitdown_docx_result_path)
def docling_expected():
    return _get_raw_content(docling_result_path)
def textract_analyze_result():
    return _get_raw_content(textract_analyze_result_path)
def textract_detect_result():
    return _get_raw_content(textract_detect_result_path)

