# -*- coding: utf-8 -*-
"""
    pdfWriter.py

    Test write to pdf class

    :copyright: (c) 2018 by Zerodha Technology.
    :license: see LICENSE for details.
"""
import pytest
from mock import patch

from pdf_text_overlay import ConditionalCoordinatesNotFound
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfFileWriter
from PyPDF2.pdf import PageObject


class TestWriteToPDF:

    def test_instantiation(self, pdf_writer_inst):
        assert pdf_writer_inst.original_pdf is not None
        assert pdf_writer_inst.configuration is not None
        assert pdf_writer_inst.values is not None
        assert pdf_writer_inst.font_size == 10

    def test_create_new_pdf(self, pdf_writer_inst):
        # CASE 1: Conditional coordinates does not exist
        with pytest.raises(ConditionalCoordinatesNotFound):
            cond_coord_config = pdf_writer_inst.configuration[0]['variables']
            pdf = pdf_writer_inst.create_new_pdf(cond_coord_config)

        # CASE 2: Conditional coordinates exists
        cond_coord_config = pdf_writer_inst.configuration[0]['variables']
        pdf_writer_inst.values['gender'] = 'Male'
        pdf = pdf_writer_inst.create_new_pdf(cond_coord_config)
        assert pdf is not None

        # CASE 3: Drawing LINE shape
        configuration = [{
            "name": "",
            "draw_shape": {
                "shape": "Line",
                "r": 0,
                "g": 0,
                "b": 0,
                "x0-coordinate": 120,
                "x1-coordinate": 130,
                "y0-coordinate": 220,
                "y1-coordinate": 230,
            }
        }]
        pdf = pdf_writer_inst.create_new_pdf(configuration)
        assert pdf is not None

        # CASE 4: Drawing RECTANGLE shape
        configuration[0]["draw_shape"]["shape"] = "Rectangle"
        pdf = pdf_writer_inst.create_new_pdf(configuration)
        assert pdf is not None

        # CASE 5: Drawing image
        pdf_writer_inst.values["image"] = ImageReader(
            "https://www.google.com/images/srpr/logo11w.png"
        )
        configuration = [{
            "name": "image",
            "image": {
                "x-coordinate": 120,
                "y-coordinate": 130,
                "width": 100,
                "height": 100,
            }
        }]
        pdf = pdf_writer_inst.create_new_pdf(configuration)
        assert pdf is not None

        # CASE 6: Drawing string
        configuration = [{
            "name": "test_string",
            "value": "OVERLAY",
            "x-coordinate": 100,
            "y-coordinate": 120,
        }]
        pdf = pdf_writer_inst.create_new_pdf(configuration)
        assert pdf is not None
        # Remove value from configuration should inturn fallback to name
        del configuration[0]["value"]
        pdf_writer_inst.values["test_string"] = "OVERLAY"
        pdf = pdf_writer_inst.create_new_pdf(configuration)
        assert pdf is not None

    @patch.object(PageObject, "mergePage")
    @patch.object(PdfFileWriter, "addPage")
    def test_edit_and_save_pdf(self, mock_merge, mock_add, pdf_writer_inst):
        pdf_writer_inst.values['gender'] = 'Male'
        output = pdf_writer_inst.edit_and_save_pdf()
        assert output is not None
        assert mock_merge.call_count == 3
        assert mock_add.call_count == 3
