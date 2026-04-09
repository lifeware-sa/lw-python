import click
import json
import multiprocessing
from lwPython._utils import *

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
        save_markdown(markdown_text, output)

    except Exception as e:
        print(f"An error occurred: {e}")

cli.add_command(textract_to_markdown)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    cli()
