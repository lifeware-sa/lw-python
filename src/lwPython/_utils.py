from textractor.parsers import response_parser
from markitdown import MarkItDown
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions

def save_markdown(content: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def markitdown_file_to_md(path: str)-> str:
    md = MarkItDown(enable_plugins=True)
    parsing = md.convert(path)
    return parsing.text_content

def docling_pdf_to_md(path: str) -> str:
    pdf_options = PdfPipelineOptions(generate_picture_images=False)

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pdf_options)
        }
    )

    doc = converter.convert(path).document
    return doc.export_to_markdown()

def textract_json_result_to_md(textract_json_result) -> str:
    textracted = response_parser.parse(textract_json_result)
    return textracted.to_markdown()