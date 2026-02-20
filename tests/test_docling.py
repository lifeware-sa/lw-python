from . import assets
from . import expecteds

from lwPython import docling_pdf_to_md

def _test_docling_result_to_md(asset, expected: str):
    result = docling_pdf_to_md(asset)
    assert result == expected

def test_docling_to_md():
    textract_answer = assets.pdf_file_path()
    expected_result = expecteds.docling_expected()
    _test_docling_result_to_md(textract_answer, expected_result)