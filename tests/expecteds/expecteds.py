from pathlib import Path

expecteds_path = Path(__file__).parent

textract_analyze_result_path = expecteds_path / 'expected_textract_analyze_result.md'
textract_detect_result_path = expecteds_path / 'expected_textract_detect_result.md'

def _get_raw_content(path: str):
    with open(path, 'r') as input:
        return input.read()
    
def textract_analyze_result():
    return _get_raw_content(textract_analyze_result_path)
def textract_detect_result():
    return _get_raw_content(textract_detect_result_path)

