# -*- coding: utf-8 -*-
"""
    conftest.py

    :copyright: (c) 2018 by Zerodha Technology.
    :license: see LICENSE for details.
"""
import os
import json
import pytest
import random
import string

from pdf_text_overlay.pdfWriter import WriteToPDF


def fp(rel_path):
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            rel_path
        )
    )


@pytest.fixture
def pdf_writer_inst():
    configuration, = json.loads(open(fp("./configuration.json")).read()),
    data = {}
    for config in configuration:
        for var in config["variables"]:
            data[var["name"]] = "".join([
                random.choice(string.ascii_letters)
                for n in range(10)
            ])
    return WriteToPDF(
        original_pdf=open(fp("./blank.pdf"), "rb"),
        configuration=configuration,
        values=data,
        font=open(fp("../examples/Lato-Italic.ttf"), "rb")
    )
