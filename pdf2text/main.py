from pathlib import Path
from pdf2image import convert_from_path
import pyocr
import pyocr.builders
import sys

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("OCR tools is not found")
    sys.exit(1)
tool = tools[0]
lan = "jpn"

f_name = "sample"
pdf_path = Path(f"../data/{f_name}.pdf")
txt_path = Path(f"../data/{f_name}.txt")

pages = convert_from_path(str(pdf_path), 300)

txt = ""
for i, page in enumerate(pages):
    txt = txt + tool.image_to_string(page, lang=lan, builder=pyocr.builders.TextBuilder(tesseract_layout=6))

# テキストファイルに書き出し
with open(txt_path, mode="w") as f:
    f.write(txt)
print("Process completed!")
