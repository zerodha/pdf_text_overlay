# -*- coding: utf-8 -*-
"""
    pdfWriter.py

    Test write to pdf class

    :copyright: (c) 2018 by Zerodha Technology.
    :license: see LICENSE for details.
"""
import pytest
from mock import patch

from pdf_text_overlay import ConditionalCoordinatesNotFound, InvalidFontError
from pdf_text_overlay.pdfWriter import WriteToPDF, pdf_writer
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter
from PyPDF2._page import PageObject


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

    @patch.object(PageObject, "merge_page")
    @patch.object(PdfWriter, "add_page")
    def test_edit_and_save_pdf(self, mock_add, mock_merge, pdf_writer_inst):
        pdf_writer_inst.values['gender'] = 'Male'
        output = pdf_writer_inst.edit_and_save_pdf()
        assert output is not None
        assert mock_merge.call_count == 3
        assert mock_add.call_count == 3

    def test_custom_font_size_is_applied(self, pdf_writer_inst):
        """font_size should be forwarded to the underlying canvas font."""
        pdf_writer_inst.font_size = 24
        pdf_writer_inst.values['gender'] = 'Male'
        configuration = pdf_writer_inst.configuration[0]['variables']

        with patch.object(canvas.Canvas, "setFont") as mock_set_font:
            pdf_writer_inst.create_new_pdf(configuration)

        mock_set_font.assert_any_call('font_style', 24)

    def test_default_font_size_is_ten(self, pdf_writer_inst):
        assert pdf_writer_inst.font_size == 10


class TestFontValidation:

    def test_missing_font_raises_invalid_font_error(self, blank_pdf):
        with pytest.raises(InvalidFontError):
            WriteToPDF(
                original_pdf=blank_pdf,
                configuration=[],
                values={},
                font=None,
            )

    def test_wrong_type_font_raises_invalid_font_error(self, blank_pdf):
        with pytest.raises(InvalidFontError):
            WriteToPDF(
                original_pdf=blank_pdf,
                configuration=[],
                values={},
                font=12345,
            )

    def test_nonexistent_font_path_raises_invalid_font_error(self, blank_pdf):
        with pytest.raises(InvalidFontError):
            WriteToPDF(
                original_pdf=blank_pdf,
                configuration=[],
                values={},
                font="/no/such/font.ttf",
            )

    def test_font_file_object_is_accepted(self, blank_pdf, font_path):
        with open(font_path, "rb") as font_file:
            inst = WriteToPDF(
                original_pdf=blank_pdf,
                configuration=[],
                values={},
                font=font_file,
            )
        assert inst is not None

    def test_font_path_string_is_accepted(self, blank_pdf, font_path):
        inst = WriteToPDF(
            original_pdf=blank_pdf,
            configuration=[],
            values={},
            font=font_path,
        )
        assert inst is not None


class TestPdfWriter:

    @patch("pdf_text_overlay.pdfWriter.WriteToPDF")
    def test_forwards_font_and_font_size(self, mock_write_to_pdf):
        mock_instance = mock_write_to_pdf.return_value

        pdf_writer("original_pdf", [], {}, "font", font_size=24)

        mock_write_to_pdf.assert_called_once_with(
            "original_pdf", [], {}, "font", 24
        )
        mock_instance.edit_and_save_pdf.assert_called_once()

    @patch("pdf_text_overlay.pdfWriter.WriteToPDF")
    def test_default_font_size_forwarded(self, mock_write_to_pdf):
        pdf_writer("original_pdf", [], {}, "font")

        mock_write_to_pdf.assert_called_once_with(
            "original_pdf", [], {}, "font", 10
        )
