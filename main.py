import json
import click

@click.command((name='textract-to-md'))
@click.argument('from', type=click.Path(exists=True))
@click.argument('to', type=click.Path())
def textract_to_markdown(input, output):
    try:
        with open(input, 'r') as json_file:
            data = json.load(json_file)
        
        with open(output, 'w') as md_file:
            # You can customize this to the structure of your JSON
            md_file.write("# Extracted Content\n\n")
            for key, value in data.items():
                md_file.write(f"## {key}\n\n{value}\n\n")

        print(f"Markdown file successfully created at {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    textract_to_markdown()
