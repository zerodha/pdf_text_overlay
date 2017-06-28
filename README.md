# pdf_writer

## Exapmle

import json
from pdf_writer import pdfWriter

original_pdf = file("file_name.pdf", "rb")<br>
font = file("font_name.ttf", "rb")<br>

### output = pdfWriter(original_pdf, configuration, data, font)<br>

outputStream = file("output.pdf", "wb")<br>
output.write(outputStream)<br>
outputStream.close()
