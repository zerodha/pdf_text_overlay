[![Build Status](https://img.shields.io/travis/zerodhatech/pdf_text_overlay.svg)](https://travis-ci.org/zerodhatech/pdf_text_overlay)

# pdf_text_overlay

pdf_text_overlay lets you
* add text to the existing pdf
* generate pdf from jinja HTML template

## Installation

```pip install pdf_text_overlay```

or Clone the repository and run

```python setup.py install```

### Example: PDF text overlay

```python
import json
from pdf_text_overlay import pdf_writer

configuration = json.loads("""[
   {
      "page_number":1,
      "variables":[
         {
            "name":"name",
            "x-coordinate":180,
            "y-coordinate":665,
            "font_size":8
         },
         {
            "name":"gender",
            "conditional_coordinates":[
               {
                  "if_value":"Male",
                  "print_pattern":"*",
                  "x-coordinate":96,
                  "y-coordinate":577
               },
               {
                  "if_value":"Female",
                  "print_pattern":"*",
                  "x-coordinate":132,
                  "y-coordinate":577
               },
               {
                  "if_value":"Transgender",
                  "print_pattern":"*",
                  "x-coordinate":178,
                  "y-coordinate":577
               }
            ]
         }
      ]
   },
   {
      "page_number":2,
      "variables":[
         {
            "name":"bank_name",
            "x-coordinate":135,
            "y-coordinate":326
         }
      ]
   },
   {
      "page_number":0,
      "variables":[
         {
            "name":"user_ifsc",
            "x-coordinate":400,
            "y-coordinate":6
         }
      ]
   }
]""")

data = json.loads("""{
   "name":"Goli",
   "gender":"Male",
   "user_ifsc":"HDFC0004421",
   "bank_name":"HDFC BANK"
}""")

original_pdf = file("file_name.pdf", "rb")
font = file("font_name.ttf", "rb")
output = pdf_writer(original_pdf, configuration, data, font)
outputStream = file("output.pdf", "wb")
output.write(outputStream)
outputStream.close()
```

### Example: PDF from template
```
from pdf_text_overlay import pdf_from_template

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
```

## Built With

* [pyPdf](http://pybrary.net/pyPdf/) - A Pure-Python library built as a PDF toolkit
* [reportlab](https://www.reportlab.com/) - An Open Source Python library for generating PDFs and graphics.
* [pdfkit](https://pypi.org/project/pdfkit/) -  Wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit

## Contributing

Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/shridarpatil/pdf_text_overlay/tags).

## License

This project is licensed under the MIT License
