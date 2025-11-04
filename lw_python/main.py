import click
import json
# from . import textract

from textractor.parsers import response_parser
def textract_json_result_to_md(textract_json_result) -> str:
    textracted = response_parser.parse(textract_json_result)
    return textracted.to_markdown()

@click.group()
def cli():
    pass

@click.command(name='textract-to-md')
@click.option('-f', '--from', 'input', type=click.Path(exists=True), help="Input JSON file")
@click.option('-t', '--to', 'output', type=click.Path(), help="Output Markdown file")
def textract_to_markdown(input, output):
    try:
        with open(input, 'r') as json_file:
            markdown_text = textract_json_result_to_md(json.load(json_file))
            # markdown_text = textract.textract_json_result_to_md(json.load(json_file))

        with open(output, 'w') as md_file:
            md_file.write(markdown_text)

    except Exception as e:
        print(f"An error occurred: {e}")

cli.add_command(textract_to_markdown)

if __name__ == '__main__':
    cli()
