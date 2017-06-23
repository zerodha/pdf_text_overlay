from distutils.core import setup
setup(
  name = 'pdf_writer',
  packages = ['pdf_writer'], # name of the package
  version = '0.1',
  description = 'Python library to write text on top of PDF',
  author = 'Shridhar Patil',
  author_email = 'shridharpatil2792@gmail.com',
  url = 'https://github.com/shridarpatil/pdf_writer', #URL to the github repo
  download_url = 'https://github.com/shridarpatil/pdf_writer/archive/0.1.tar.gz',
  keywords = ['pdf writer', 'Pdf Editor'], # arbitrary keywords
  classifiers = [],
  install_requires=[
              'pyPdf', 'reportlab'
            ]
)
