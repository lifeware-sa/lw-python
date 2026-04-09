def save_markdown(content: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

# def markitdown_file_to_md(path: str)-> str:
#     from markitdown import MarkItDown
#     md = MarkItDown(enable_plugins=True)
#     parsing = md.convert(path)
#     return parsing.text_content

# def docling_pdf_to_md(path: str) -> str:
#     from docling.datamodel.base_models import InputFormat
#     from docling.datamodel.pipeline_options import PdfPipelineOptions
#     from docling.document_converter import DocumentConverter, PdfFormatOption

#     pipeline_options = PdfPipelineOptions()
#     pipeline_options.do_ocr = False

#     converter = DocumentConverter(
#         format_options={
#             InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
#         }
#     )
#     doc = converter.convert(path).document
#     return doc.export_to_markdown()

def textract_json_result_to_md(textract_json_result) -> str:
    from textractor.parsers import response_parser
    textracted = response_parser.parse(textract_json_result)
    return textracted.to_markdown()