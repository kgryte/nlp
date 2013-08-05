#!/usr/bin/env python
# coding: utf-8

# Doc String:
"""Module to tokenize HTML text.

To tokenize is to split a string of text. We map string and unicode objects to lists of unicode objects.

The method for tokenization is application-dependent, meaning no single best way to tokenize exists. Each implementation needs to be tailored to a context.

The basic flow is as follows:

[1] Define a list of regular expression strings (tuple)

[2] Place [1] into a compiled regular expression object

[3] Tokenize by finding all matching patterns: re.findall(s)

[*] Before tokenizing, options can be set to tailor behavior; e.g., preserving case, etc.

Sources:
    - Christopher Potts: http://sentiment.christopherpotts.net/tokenizing.html

"""

# Module version number:
__version__ = '0.1.0'

# Required modules:
import re               # regular expression module
import htmlentitydefs   # HTML tag definitions

# Define exceptions; we first define a base class which inherits from 'exception' and then derive any further errors from this base class. This is so we can name the errors and provide any tailored error handling:
class TokenizerError(Exception):
    """Base class for errors in the tokenize module"""

    pass

# Define the tokenizer class:
class Tokenizer(object): # inherit from the base object
    """Class for Tokenizer instances


    """

    # Define class level attributes:

    # Define the regular expression strings:
    _patterns = (
        r"""
        # HTML tags:
        <[^>]+>
        """,
        r"""
        # Words with apostrophes or dashes:
        (?:[a-z][a-z'\-_]+[a-z])
        |
        # Numbers, including fractions and decimals:
        (?:[+\-]?\d+[,/.:-]\d+[+\-]?)
        |
        # Words without apostrophes or dashes:
        (?:[\w_]+)
        |
        # Everything else that is not whitespace:
        (?:\S)
        """
        )

    # Compile the regular expression object:
    _regex = re.compile(r"""(%s)""" % "|".join(_patterns), re.VERBOSE | re.I | re.UNICODE )

    # Regular expression object just for HTML tags:
    _regex_html = re.compile(r"""<[^>]+>""")

    # Compile additional objects to convert HTML encoded entities to Unicode:
    _regex_html_alpha = re.compile(r"&\w+;")
    _regex_html_numeric = re.compile(r"&#\d+;")
    _amp = "&amp;"

    # Regular expression object for (normal) sentence termination:
    _regex_sentence = re.compile(r""" *([\.\?!][\'"\)\]]*) *""")

    # Define the initialization method:
    def __init__(self):
        """Initialize instance properties"""

        # Remove all HTML markup?
        self._removeHTML = True

        # Split text into individual sentences?
        self._splitSentences = True

    def tokenize(self, string):
        """Tokenize a string"""

        # Convert the string to unicode:
        text = self._unicode(string)

        # Convert any HTML entities to unicode:
        text = self._html2unicode(text)

        # Remove HTML tags:
        if self._removeHTML:
            text = self.__removeHTML(text)

        # Split text into sentences:
        if self._splitSentences:
            text = self.__splitSentences(text)
        else:
            text = [text] # single element list

        # Tokenize the text:
        tokens = []
        for string in text:
            tokens.append(self._regex.findall(string))

        return tokens

    # Unicode conversion:
    def _unicode(self, string):
        """Convert a string to unicode"""

        try:
            string = unicode(string)
        except UnicodeDecodeError:
            string = str(string).encode('string_escape')
            string = unicode(string)

        return string

    # HTML to unicode conversion:
    def _html2unicode(self, string):
        """Convert HTML entities to unicode"""

        # Encode any numeric encodings:

        # Get the digits:
        entities = set(self._regex_html_numeric.findall(string))

        if len(entities) > 0:
            for entity in entities:

                # Remove the &# prefix and the ending ; such that we extract only the entity number:
                num = entity[2:-1]

                try:
                    # Replace any numeric encodings with their unicode string:
                    num = int(num)
                    string = string.replace(entity, unichr(num))
                except:
                    pass

        # Encode any alpha character encodings:

        # Get the entities:
        entities = set(self._regex_html_alpha.findall(string))

        # Exclude any entities which are the ampersand itself:
        entities = filter((lambda x : x != self._amp), entities)

        for entity in entities:

            # Remove the & prefix and ending ; to extract only the entity name (e.g., < is encoded as &lt; and the name we then want to extract is just lt):
            name = entity[1:-1]

            try:
                # Replace the entity with its HTML symbol:
                string = string.replace(entity, unichr(htmlentitydefs.name2codepoint[name]))
            except:
                pass

            # Replace any ampersands:
            string = string.replace(self._amp, " and ")

        # Return the unicode string:
        return string

    def __removeHTML(self, string):
        """Remove HTML tags from string"""

        return self._regex_html.sub('', string)

    def __splitSentences(self, text):
        """Split text into sentences"""

        return self._regex_sentence.split(text)

