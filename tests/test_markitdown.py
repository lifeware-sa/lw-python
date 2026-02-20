from . import assets
from . import expecteds

from lwPython import markitdown_file_to_md

def _test_markitdown_result_to_md(asset, expected: str):
    result = markitdown_file_to_md(asset)
    assert result == expected

def test_markitdown_pdf_to_md():
    textract_answer = assets.pdf_file_path()
    expected_result = expecteds.markitdown_pdf_expected()
    _test_markitdown_result_to_md(textract_answer, expected_result)

def test_markitdown_docx_to_md():
    textract_answer = assets.docx_file_path()
    expected_result = expecteds.markitdown_docx_expected()
    _test_markitdown_result_to_md(textract_answer, expected_result)