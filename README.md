# pdf_text_overlay

pdf_text_overlay is a python library to write a text on top of pdf. <br>

pdf_text_overlay paramaters 
 - original_pdf (Pdf file object)
 - configuration (configuration data)
 - data (The data which needs to be writen on the pdf)
 - font (Font file object - the font that is to be used to write the text on pdf)
 
### Example
```
import json
from pdf_writer import pdfWriter
configuration = json.loads("""
   	
    [{
      "page_number": 2,
      "variables":[
       	{
          "name": "name",
          "x-coordinate": 180,
          "y-coordinate": 665,
          "font_size": 8,
        },
     		{
       	  "name": "gender",
       		"conditional_coordinates":[    
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
    },
    {
      "page_number": 3,
      "variables": [
          {
            "name": "bank_name",
            "x-coordinate": 135,
            "y-coordinate": 326
          }
        ]
    },
    {
      "page_number": 1,
      "variables": [
         {
            "name": "user_ifsc",
            "x-coordinate": 400,
            "y-coordinate": 6
          }
        ] 
      }
    ]"""

data = json.loads("""
    {	
      "name": "Goli",
      "gender": "Male",
      "user_ifsc": "HDFC0004421",
      "bank_name": "HDFC BANK"
    }
""")
original_pdf = file("file_name.pdf", "rb")
font = file("font_name.ttf", "rb")
output = pdfWriter(original_pdf, configuration, data, font)
outputStream = file("output.pdf", "wb")
output.write(outputStream)
outputStream.close()```
