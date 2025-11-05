from . import assets
from . import expecteds

from ..textract import textract_json_result_to_md

def _test_textract_result_to_md(asset, expected: str):
    result = textract_json_result_to_md(asset)
    assert result == expected

def test_textract_detect_result_to_md():
    textract_answer = assets.textract_detect_result()
    expected_result = expecteds.textract_detect_result()
    _test_textract_result_to_md(textract_answer, expected_result)

def test_textract_analyze_result_to_md():
    textract_answer = assets.textract_analyze_result()
    expected_result = expecteds.textract_analyze_result()
    _test_textract_result_to_md(textract_answer, expected_result)
    