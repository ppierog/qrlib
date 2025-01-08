import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "qrlib",
    version = "1.3.0",
    author = "Miguel Paolino",
    maintainer="Piotr Pierog",
    download_url="http://github.com/ppierog/qrlib",
    author_email = "mpaolino@ideal.com.uy",
    description = ("QR Image and PDF generation library"),
    license = "Propietary",
    keywords = "qr library qrlib ideal fancy",
    url = "http://github.com/ppierog/qrlib",
    packages=['qrlib', 'qrlib.lib', 'qrlib.fonts', 
              'qrlib.tests'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 1 - Stable",
        "Topic :: Utilities",
        ],
    package_dir={'qrlib': 'qrlib'},
    package_data={'qrlib': ['static/images/*',
                            'static/eyes/circle/*',
                            'static/eyes/cushion/*',
                            'static/eyes/default/*',
                            'static/eyes/diamond/*',
                            'static/eyes/dots/*',
                            'static/eyes/heavyround/*',
                            'static/eyes/leaf/*',
                            'static/eyes/left_eye/*',
                            'static/eyes/right_eye/*',
                            'static/eyes/shield/*',
                            'static/eyes/sieve/*',
                            'static/eyes/star/*',
                            'static/styles/arrow/*',
                            'static/styles/circle/*',
                            'static/styles/classic/*',
                            'static/styles/default/*',
                            'static/styles/heavyround/*',
                            'static/styles/lightround/*',
                            'static/styles/sieve/*']},
    install_requires=['pillow', 'unittest2', 'zbarlight', 'reportlab', 'CairoSVG']
    )
