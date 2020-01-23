import json

from pdf_text_overlay import pdf_writer, pdf_from_template

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

original_pdf = open("Blank_Pdf.pdf", "rb")
font = open("Lato-Italic.ttf", "rb")
output = pdf_writer(original_pdf, configuration, data, font)
outputStream = open("output.pdf", "wb")
output.write(outputStream)
outputStream.close()

# Demo: pdf from jinja template
jinja_data = {
    "title": "Jinja PDF Demo",
    "stocks": [
        {"symbol": "PIEDPIPER", "qty": 100, "price": 2500},
        {"symbol": "HOOLI", "qty": 100, "price": 2500},
    ]
}

with open("template.html") as htmlfile:
    html_str = htmlfile.read()
    filecontent = pdf_from_template(html_str, jinja_data)
    f = open('output.pdf', 'wb')
    f.write(filecontent)
    f.close()
