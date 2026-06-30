 <a href="https://zerodha.tech"><img src="https://zerodha.tech/static/images/github-badge.svg" align="right" /></a>
[![Build Status](https://img.shields.io/travis/zerodhatech/pdf_text_overlay.svg)](https://travis-ci.org/zerodhatech/pdf_text_overlay)

# pdf_text_overlay

pdf_text_overlay lets you
* add text to the existing pdf
* generate pdf from jinja HTML template

## Installation

```pip install pdf_text_overlay```

or Clone the repository and run

```python setup.py install```

### Prerequisites

`pdf_text_overlay` uses [pdfkit](https://pypi.org/project/pdfkit/) to generate PDFs from HTML templates. `pdfkit` is a wrapper and does not render PDFs itself — it requires the external [wkhtmltopdf](https://wkhtmltopdf.org/) binary to be installed separately and available on your system `PATH`.

Install `wkhtmltopdf` for your platform:

* **Linux (Debian/Ubuntu)**

  ```sh
  sudo apt-get install wkhtmltopdf
  ```

* **macOS (Homebrew)**

  ```sh
  brew install --cask wkhtmltopdf
  ```

* **Windows**

  Download and run the installer from the [wkhtmltopdf downloads page](https://wkhtmltopdf.org/downloads.html), then add the installation directory (e.g. `C:\Program Files\wkhtmltopdf\bin`) to your system `PATH`.

After installation, verify it's accessible by running `wkhtmltopdf --version` from a terminal. If the command is not found, double-check that the binary's location has been added to your `PATH`.

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

original_pdf = open("file_name.pdf", "rb")
font = open("font_name.ttf", "rb")
output = pdf_writer(original_pdf, configuration, data, font, font_size=10)
outputStream = open("output.pdf", "wb")
output.write(outputStream)
outputStream.close()
```

`pdf_writer(original_pdf, configuration, data, font, font_size=10)` parameters:

* `font` (required) - either a path (`str`) to a `.ttf` file, or a file-like object opened in binary mode, e.g. `open("font.ttf", "rb")`. Passing `None` or an invalid path/type raises `InvalidFontError` with a clear message instead of an obscure ReportLab error.
* `font_size` (optional, default `10`) - the default font size used to draw text. It can be overridden per field by setting `"font_size"` on that field's entry in `configuration` (see the `"name"` field above).

### Example: PDF from template
```python
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
