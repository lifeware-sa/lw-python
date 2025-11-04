from pathlib import Path
import json

from ..textract import textract_json_result_to_md

test_dir = Path(__file__).parent
assets_path = test_dir / 'assets'

def test_textract_json_result_to_md():
    with open(assets_path / 'textract_result.json', 'r') as textract_result:
        result = textract_json_result_to_md(json.load(textract_result))
    with open(assets_path / 'textract_result.md', 'w') as res:
        res.write(result)
