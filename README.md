# pdf_writer

## Exapmle<br>

import json<br>
from pdf_writer import pdfWriter<br>

configuration = json.loads("""[<br>
	  {<br>
	    "page_number": 2, <br>
	    "variables": [<br>
	      {<br>
		"name": "name",<br>
		 "x-coordinate": 180,<br>
		"y-coordinate": 665<br>
	      },<br>
	      {<br>
		"name": "father_spouse",<br>
		 "x-coordinate": 180,<br>
		"y-coordinate": 625<br>
	      },<br>
	      {<br>
		"name": "mother_name",<br>
		 "x-coordinate": 180,<br>
		"y-coordinate": 611<br>
	      },<br>
	      {<br>
		"name": "gender", <br>
		"conditional_coordinates": [<br>

		  {<br>
		    "if_value": "Male",<br>
		    "print_pattern": "*",<br>
		    "x-coordinate": 96,<br>
		    "y-coordinate": 577<br>
		  },<br>
		  {<br>
		    "if_value": "Female",<br>
		    "print_pattern": "*",<br>
		    "x-coordinate": 132,<br>
		    "y-coordinate": 577<br>
		  },<br>
		  {<br>
		    "if_value": "Transgender",<br>
		    "print_pattern": "*",<br>
		    "x-coordinate": 178,<br>
		    "y-coordinate": 577<br>
		  }<br>
		]<br>
	      }	<br>
	    ]<br>
	  }]""")<br>

data = json.loads("""{<br>
	"name": "John",<br>
	"father_spouse": "Micheal",<br>
	"mother_name": "Merry",<br>
	"gender": "Male"<br>
}""")<br>

original_pdf = file("file_name.pdf", "rb")<br>
font = file("font_name.ttf", "rb")<br>

###output = pdfWriter(original_pdf, configuration, data, font)<br>

outputStream = file("output.pdf", "wb")<br>
output.write(outputStream)<br>
outputStream.close()
