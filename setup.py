"""Setup.py."""
# import ast
# import re

from setuptools import setup

# _version_re = re.compile(r'__version__\s+=\s+(.*)')

# with open('./pdf_text_overlay/__init__.py', 'rb') as f:
#     version = str(ast.literal_eval(_version_re.search(
#         f.read().decode('utf-8'))))
version = '0.3.1'

setup(
    name='pdf_text_overlay',
    packages=['pdf_text_overlay'],  # name of the package
    version=version,
    description='Python library to write text on top of PDF',
    author='Shridhar Patil',
    author_email='shridharpatil2792@gmail.com',
    url='https://github.com/shridarpatil/pdf_writer',  # URL to the github repo
    download_url='https://github.com/shridarpatil/pdf_writer/archive/%s.tar.gz' % version, # noqa
    keywords=['pdf writer', 'Pdf Editor'],  # arbitrary keywords
    classifiers=[],
    install_requires=['pyPdf', 'reportlab'],
)
