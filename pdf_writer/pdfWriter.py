import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class WriteToPdf:
	def __init__(cls, original_pdf, configuration, values, font):
		pdfmetrics.registerFont(TTFont('font_style', font))
		cls.values = values
		cls.original_pdf = original_pdf
		cls.configuration = configuration

	# create a new PDF with Reportlab
	def create_pew_pdf(cls, configuration):
		
		pdf = StringIO.StringIO()
		values = cls.values
		
		can = canvas.Canvas(pdf, pagesize=letter)
		can.setFont('font_style', 10)

		for config_data in configuration:
			
			key = config_data['name']

			if 'conditional_coordinates' in config_data:
				for co_ordinates in config_data['conditional_coordinates']:
					if co_ordinates['if_value'] == values[key]:
						x = co_ordinates['x-coordinate']
						y = co_ordinates['y-coordinate']
						if co_ordinates['print_pattern'] == False:
							value = co_ordinates['if_value']
						else :
							value = co_ordinates['print_pattern']
						
						if 'font_size' in config_data:
							can.setFont('font_style', config_data["font_size"])
					
			else :
				x = config_data['x-coordinate']
				y = config_data['y-coordinate']
				value = values[key]
				if 'font_size' in config_data:
					can.setFont('font_style', config_data["font_size"])
			can.drawString(x, y, value)
		
		can.save()
		
		return pdf

	def parse_configuration(cls, page_number):
		configuration = cls.configuration
		for i in range(len(configuration)) : 
			if configuration[i]['page_number'] == page_number :
				return configuration[i]['variables']
		return -1



	def edit_and_save_pdf(cls):
		original_pdf = PdfFileReader(cls.original_pdf)
		output = PdfFileWriter()
		for i in range(original_pdf.numPages):
			configuration = cls.parse_configuration(i)
			page = original_pdf.getPage(i)
			if configuration != -1 :
				new_pdf = PdfFileReader(cls.create_pew_pdf(configuration))
				page.mergePage(new_pdf.getPage(0))
			
			output.addPage(page)
		return output

def pdfWriter(original_pdf, configuration, data, font):
  x = WriteToPdf(original_pdf, configuration, data, font)
  output = x.edit_and_save_pdf()
  return output

version = 0.1