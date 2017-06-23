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
      },
		{
        "name": "marital_status", 
        "conditional_coordinates": [
          
          {
            "if_value": "Married",
            "print_pattern": "*",
            "x-coordinate": 364.5,
            "y-coordinate": 577
          },
          {
            "if_value": "Single",
            "print_pattern": "*",
            "x-coordinate": 325,
            "y-coordinate": 577
          },
          {
            "if_value": "Other",
            "print_pattern": "*",
            "x-coordinate": 412.5,
            "y-coordinate": 577
          }
        ]
      },
      {
        "name": "mob_phone",
         "x-coordinate": 370,
        "y-coordinate": 377
      },
			{
        "name": "email",
         "x-coordinate": 360,
        "y-coordinate": 364
      },
			{
        "name": "user_comm_addr_line1",
         "x-coordinate": 85,
        "y-coordinate": 320
      },
			{
        "name": "user_comm_addr_line2",
         "x-coordinate": 65,
        "y-coordinate": 305
      },
			{
        "name": "user_comm_city",
        "x-coordinate": 90,
        "y-coordinate": 292
      },
			{
        "name": "user_comm_district",
        "x-coordinate": 310,
        "y-coordinate": 292
      },
			{
        "name": "user_comm_pincode",
        "x-coordinate": 490,
        "y-coordinate": 292
      },
			{
        "name": "user_comm_state",
        "x-coordinate": 120,
        "y-coordinate": 279
      },
			{
        "name": "user_comm_country",
        "x-coordinate": 490,
        "y-coordinate": 279
      },
			{
        "name": "user_pan",
        "x-coordinate": 88,
        "y-coordinate": 461
      },
      {
        "name": "corr_residence_proof",
        "x-coordinate": 390,
        "y-coordinate": 265
      },
			{
        "name": "dob",
        "x-coordinate": 492,
        "y-coordinate": 580,
		"font_size": 8
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
      },
      {
        "name": "user_ifsc",
        "x-coordinate": 420,
        "y-coordinate": 272
      },
      {
        "name": "bank_address",
        "x-coordinate": 125,
        "y-coordinate": 312
      },
      {
        "name": "user_account_no",
        "x-coordinate": 125,
        "y-coordinate": 285
      },
      {
        "name": "bank_micr",
        "x-coordinate": 125,
        "y-coordinate": 273
      },
      {
        "name": "bank_acc_type", 
        "conditional_coordinates": [
          
          {
            "if_value": "Current",
            "print_pattern": "*",
            "x-coordinate": 194,
            "y-coordinate": 346
          },
          {
            "if_value": "Savings",
            "print_pattern": "*",
            "x-coordinate": 135,
            "y-coordinate": 346
          },
          {
            "if_value": "Other",
            "print_pattern": "*",
            "x-coordinate": 247,
            "y-coordinate": 346
          },
          {
            "if_value": "NRE",
            "print_pattern": "*",
            "x-coordinate": 409.5,
            "y-coordinate": 346
          },
          {
            "if_value": "NRO",
            "print_pattern": "*",
            "x-coordinate": 455,
            "y-coordinate": 346
          }
        ]
      },
      {
        "name": "occupation", 
        "conditional_coordinates": [
          
          {
            "if_value": "Private Sector",
            "print_pattern": "*",
            "x-coordinate": 98,
            "y-coordinate": 147
          },
          {
            "if_value": "Agriculturist",
            "print_pattern": "*",
            "x-coordinate": 502,
            "y-coordinate": 147
          },
          {
            "if_value": "Public Sector",
            "print_pattern": "*",
            "x-coordinate": 182,
            "y-coordinate": 147
          },
          {
            "if_value": "Government Service",
            "print_pattern": "*",
            "x-coordinate": 291,
            "y-coordinate": 147
          },
          {
            "if_value": "Business",
            "print_pattern": "*",
            "x-coordinate": 353,
            "y-coordinate": 147
          },
          {
            "if_value": "Professional",
            "print_pattern": "*",
            "x-coordinate": 424,
            "y-coordinate": 147
          },
          {
            "if_value": "Retired",
            "print_pattern": "*",
            "x-coordinate": 555,
            "y-coordinate": 147
          },
          {
            "if_value": "Self Employed",
            "print_pattern": "*",
            "x-coordinate": 239,
            "y-coordinate": 128
          },
          {
            "if_value": "Housewife",
            "print_pattern": "*",
            "x-coordinate": 555,
            "y-coordinate": 147
          },
          {
            "if_value": "Student",
            "print_pattern": "*",
            "x-coordinate": 239,
            "y-coordinate": 128
          }

        ]
      },
            {
        "name": "user_net_worth", 
        "conditional_coordinates": [
          
          {
            "if_value": "<1",
            "print_pattern": "*",
            "x-coordinate": 112,
        	"y-coordinate": 207
          },
          {
            "if_value": "1-5",
            "print_pattern": "*",
            "x-coordinate": 190,
            "y-coordinate": 147
          },
          {
            "if_value": "5-10",
            "print_pattern": "*",
            "x-coordinate": 281,
            "y-coordinate": 207
          },
          {
            "if_value": "10-25",
            "print_pattern": "*",
            "x-coordinate": 376,
            "y-coordinate": 207
          },
          {
            "if_value": ">25",
            "print_pattern": "*",
            "x-coordinate": 466,
            "y-coordinate": 207
          }
        ]
      },
        {
        	"name": "user_net_date",
        	"x-coordinate": 125,
        	"y-coordinate": 190
      	},
      	{
        	"name": "user_net_worth",
        	"x-coordinate": 250,
        	"y-coordinate": 190
      	},
        {
        	"name": "user_addr_line1",
        	"x-coordinate": 90,
        	"y-coordinate": 767
      	},
      	{
        	"name": "user_addr_line2",
        	"x-coordinate": 50,
        	"y-coordinate": 752
      	},
      	{
        	"name": "user_city",
        	"x-coordinate": 100,
        	"y-coordinate": 738
      	},
      	{
        	"name": "user_district",
        	"x-coordinate": 310,
        	"y-coordinate": 738
      	},
      	{
        	"name": "user_pincode",
        	"x-coordinate": 490,
        	"y-coordinate": 738
      	},
      	{
        	"name": "user_state",
        	"x-coordinate": 115,
        	"y-coordinate": 725
      	},
      	{
        	"name": "user_country",
        	"x-coordinate": 490,
        	"y-coordinate": 725
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
]""")


data = json.loads("""{
	"client_id": "",
  "dp_id" : "",
	"pep": "NO",
	"rgess": "NO",
	"dis": "OPTION2",
	"app_id": "115917",
	"honorific": "MR",
	"name": "Goli",
	"last_name": "Sunil",
	"dob": "14-11-1988",
	"gender": "Male",
	"marital_status": "Married",
	"mob_phone": "9481309281",
	"email": "sunil.goli@zerodha.com",
	"father_spouse": "MALLESHWAR RAO",
	"father_last_name": "GOLI",
	"mother_name": "MANI",
	"mother_last_name": "GOLI",
	"user_pincode": "584123",
	"user_city": "RAICHUR",
	"user_district": "RAICHUR",
	"user_state": "KARNATAKA",
	"user_country": "India",
	"user_addr_line1": "S/O MALLESHWAR RAO G, R/O SAI GOKUL CAMP,",
	"user_addr_line2": "MALLAT POST, TQ MANVI, DT-RAICHUR",
	"corr_residence_proof": "Bank Account Statement/Passbook",
	"user_comm_same": "1",
	"user_comm_pincode": "560078",
	"user_comm_city": "Bangalore",
	"user_comm_district": "Bangalore",
	"user_comm_state": "Karnataka",
	"user_comm_country": "India",
	"user_comm_addr_line1": "S/O MALLESHWAR RAO G, R/O SAI GOKUL CAMP,",
	"user_comm_addr_line2": "MALLAT POST, TQ MANVI, DT-RAICHUR",
	"perm_residence_proof": "PASSPORT",
	"user_ifsc": "HDFC0004421",
	"user_account_no": "20163305145",
	"bank_name": "HDFC BANK",
	"bank_branch": "BIKRAMGANJ",
	"bank_address": "BAHUDAR FUEL SERVICE STATION SASARAM ROAD BIKRAMGANJ BIHAR - 802212",
	"bank_acc_type": "Savings",
	"bank_micr": "0",
	"income_mode": "net",
	"gross_income": "1-5",
	"user_net_worth": "<1",
	"user_net_date": "01-07-2019",
	"occupation": "Agriculturist",
	"experience": "0",
	"user_nationality": "INDIAN",
	"residence_status": "IND",
	"user_pan": "FRMPS8034K",
	"user_aadhar": "123409876543"
}""")
# print configuration["config"]
original_pdf = file("documents/ZerodhaTD_online.pdf", "rb")
font = file("arial.ttf", "rb")
output = pdfWriter(original_pdf, configuration, data, font)
outputStream = file("output1.pdf", "wb")
output.write(outputStream)
outputStream.close()
