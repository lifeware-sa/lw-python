import unittest

from pathlib import Path

from lw_python.textract import textract_json_result_to_md

test_dir = Path(__file__).parent
assets_path = test_dir / 'assets'

class TestMath(unittest.TestCase):
    def tetest_textract_json_result_to_md(self):
        with open(assets_path / 'textract_result.json', 'r') as textract_result:
            result = textract_json_result_to_md(textract_result)
        with open(assets_path / 'textract_result.md', 'r') as res:
            res.write(result)

if __name__ == "__main__":
    unittest.main()
