#!/usr/bin/env python
# coding: utf-8

# Doc String:
"""

"""

# Module version number:
__version__ = '0.1.0'

# Required modules:
import re # regular expressions
import urllib # loading web documents
from bs4 import BeautifulSoup, Comment # document parser


# Define exceptions; we first define a base class which inherits from 'exception' and then derive any further errors from this base class. This is so we can name the errors and provide any tailored error handling:
class FileParserError(Exception):
    """Base class for errors in the fileparser module"""

    pass

# Define the FileParser class:
class FileParser(object): # inherit from the base object
    """Class for FileParser instances


    """

    def __init__(self):
        """Initialize instance properties"""



    def parse(self, url):
        """Parse a url"""

        # Open the document located the supplied url:
        sock = urllib.urlopen(url)
        document = sock.read()
        sock.close()

        # Parse the document using BeautifulSoup:
        soup = BeautifulSoup(document)

        # Remove various tags:
        tmp = [s.extract() for s in soup(['iframe', 'script', 'nav', 'style', 'noscript', 'header', 'footer', 'li'])]

        # Remove comments:
        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
        [comment.extract() for comment in comments]

        # Remove common classes and ids:
        [_class.extract() for _class in soup.findAll(attrs={'class': re.compile(r"""(nav|footer)""")})]

        # Get the text:
        return soup.body.get_text()