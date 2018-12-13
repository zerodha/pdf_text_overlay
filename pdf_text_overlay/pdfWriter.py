# -*- coding: utf-8 -*-
"""
    pdfWriter.py

    Pdf text overlay

    :copyright: (c) 2018 by Zerodha Technology.
    :license: see LICENSE for details.
"""
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from pyPdf import PdfFileReader
from pyPdf import PdfFileWriter

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


class ConditionalCoordinatesNotFound(Exception):
    """Unable to conditional coordinates"""
    pass


class WriteToPDF(object):
    """Write text on top of pdf."""

    def __init__(
        self, original_pdf, configuration, values, font=None, font_size=10
    ):
        """Initialise.

        :param original_pdf (file obj): original pdf file object
        :param configuration (dict): configuration dict
        :param values (dict): values to be printed
        :param font (file obj): font
        """
        self.original_pdf = original_pdf
        self.configuration = configuration
        self.values = values
        self.font_size = font_size

        pdfmetrics.registerFont(TTFont('font_style', font))

    def create_new_pdf(self, configuration):
        """Create a PDF with reportlab with given configuration

        :param configuration: configuration data
        """
        pdf = StringIO()

        can = canvas.Canvas(pdf, pagesize=letter)
        can.setFont('font_style', self.font_size)

        for config_data in configuration:
            try:
                required = config_data.get("required", 0)
                key = config_data['name']

                if required and not self.values[key]:
                    raise ValueError(
                        """Could not find value for key: {}""".format(key)
                    )
                self.__set_font_size(can, config_data)
                can.setStrokeColorRGB(0, 0, 0)
                can.setFillColorRGB(0, 0, 0)

                if 'conditional_coordinates' in config_data:
                    try:
                        co_ordinates, = filter(
                            lambda c: c['if_value'] == self.values[key],
                            config_data['conditional_coordinates']
                        )
                    except ValueError:
                        if required:
                            raise ConditionalCoordinatesNotFound(
                                'Could not find co-ordinates for key({}) value'
                                '{}'
                                .format(key, self.values[key])
                            )
                        else:
                            continue

                    if co_ordinates['print_pattern'] is False:
                        text = co_ordinates['if_value']
                    else:
                        text = co_ordinates['print_pattern']

                    can.drawString(
                        x=co_ordinates['x-coordinate'],
                        y=co_ordinates['y-coordinate'],
                        text=text
                    )

                elif 'draw_shape' in config_data:

                    from reportlab.lib.units import inch
                    # move the origin up and to the left

                    can.translate(inch, inch)
                    can.setStrokeColorRGB(0, 0, 0)
                    can.setFillColorRGB(
                        config_data['draw_shape']['r'],
                        config_data['draw_shape']['g'],
                        config_data['draw_shape']['b']
                    )

                    # Get the cartesian coordinates
                    x0 = config_data['draw_shape'].get('x0-coordinate')
                    x1 = config_data['draw_shape'].get('x1-coordinate')
                    y0 = config_data['draw_shape'].get('y0-coordinate')
                    y1 = config_data['draw_shape'].get('y1-coordinate')

                    if config_data['draw_shape']['shape'] == 'Line':
                        can.line(
                            x1=x0 * inch,
                            y1=y0 * inch,
                            x2=x1 * inch,
                            y2=y1 * inch
                        )
                    elif config_data['draw_shape']['shape'] == 'Rectangle':
                        fill = config_data['draw_shape'].get('fill', 1)
                        can.rect(
                            x=x0 * inch,
                            y=y0 * inch,
                            width=x1 * inch,
                            height=y1 * inch,
                            fill=fill
                        )

                elif 'image' in config_data:
                    can.drawImage(
                        image=self.values[key],
                        x=config_data['image']['x-coordinate'],
                        y=config_data['image']['y-coordinate'],
                        width=config_data['image']['width'],
                        height=config_data['image']['height'],
                        mask='auto'
                    )

                else:
                    if config_data.get('value'):
                        text = config_data['value']
                    else:
                        text = self.values[key]

                    can.drawString(
                        x=config_data['x-coordinate'],
                        y=config_data['y-coordinate'],
                        text=text
                    )
            except KeyError as e:
                if required:
                    raise e
                else:
                    pass

        can.save()

        return pdf

    def __set_font_size(self, can, config_data):
        """Set font size."""
        if 'font_size' in config_data:
            can.setFont('font_style', config_data["font_size"])

    def edit_and_save_pdf(self):
        """Return file object."""
        original_pdf = PdfFileReader(self.original_pdf)
        output = PdfFileWriter()

        config_var_map = dict(
            (config['page_number'], config['variables'])
            for config in self.configuration
        )

        # Pages begin with numeric 0
        for page_no in range(original_pdf.numPages):
            configuration = config_var_map.get(page_no)
            page = original_pdf.getPage(page_no)
            if configuration:
                new_pdf = PdfFileReader(self.create_new_pdf(configuration))
                page.mergePage(new_pdf.getPage(0))
            output.addPage(page)

        return output


def pdf_writer(original_pdf, configuration, data, font, font_size=10):
    """
    Return file object.

    :param original_pdf (file obj): original pdf file object
    :param configuration (dict): configuration dict
    :param values (dict): values to be printed
    :param font (file obj): font
    """
    x = WriteToPDF(original_pdf, configuration, data, font)
    output = x.edit_and_save_pdf()
    return output
