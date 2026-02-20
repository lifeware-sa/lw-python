from pathlib import Path
import json

assets_path = Path(__file__).parent

textract_analyze_result_path = assets_path / 'textract_analyze_result.json'
textract_detect_result_path = assets_path / 'textract_detect_result.json'

def _get_json_content(path: Path | str):
    with open(path, 'r') as input:
        return json.load(input)
    
def textract_analyze_result():
    return _get_json_content(textract_analyze_result_path)
def textract_detect_result():
    return _get_json_content(textract_detect_result_path)