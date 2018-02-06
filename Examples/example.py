import json

from pdf_text_overlay import pdf_writer

configuration = json.loads("""
    [{
      "page_number": 0,
      "variables":[
        {
            "name": "first_name",
            "x-coordinate": 130,
            "y-coordinate": 710,
            "font_size": 10
        },
        {
            "name": "last_name",
            "x-coordinate": 130,
            "y-coordinate": 695,
            "font_size": 8
        }]
}]""")

data = json.loads("""
    {
        "first_name": "Goli",
        "last_name": "Male",
        "user_ifsc": "HDFC0004421",
        "bank_name": "HDFC BANK"
    }
""")

original_pdf = file("Blank_Pdf.pdf", "rb")
font = file("Lato-Italic.ttf", "rb")
output = pdf_writer(original_pdf, configuration, data, font)
outputStream = file("output.pdf", "wb")
output.write(outputStream)
outputStream.close()
