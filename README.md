# pdf_writer

## Exapmle


import json
from pdf_writer import pdfWriter

configuration =json.loads("""[
  {
    "page_number": 2, 
    "variables": [
      {
        "name": "name",
         "x-coordinate": 180,
        "y-coordinate": 665
      },
      {
        "name": "father_spouse",
         "x-coordinate": 180,
        "y-coordinate": 625
      },
      {
        "name": "mother_name",
         "x-coordinate": 180,
        "y-coordinate": 611
      },
      {
        "name": "gender", 
        "conditional_coordinates": [
          
          {
            "if_value": "Male",
            "print_pattern": "*",
            "x-coordinate": 96,
            "y-coordinate": 577
          },
          {
            "if_value": "Female",
            "print_pattern": "*",
            "x-coordinate": 132,
            "y-coordinate": 577
          },
          {
            "if_value": "Transgender",
            "print_pattern": "*",
            "x-coordinate": 178,
            "y-coordinate": 577
          }
        ]
      }	
    ]
  }]""")


data = json.loads("""{
	"name": "Goli",
	"father_spouse": "MALLESHWAR RAO",
	"mother_name": "MANI",
	"gender": "Male"
}""")

original_pdf = file("file_name.pdf", "rb")
font = file("font_name.ttf", "rb")

output = pdfWriter(original_pdf, configuration, data, font)

outputStream = file("output.pdf", "wb")
output.write(outputStream)
outputStream.close()
