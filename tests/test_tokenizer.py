#!/usr/bin/env python
# coding: utf-8

"""Unit Tests:

To run these tests, use the following command in the Terminal from the parent directory (one-level above):

    $nosetests -w tests/ -v --with-coverage --cover-package tokenizer --cover-html --cover-html-dir tokenizer-coverage

*where the $ sign indicates the prompt and should not be included in the command.

-w : change the working directory
tests/ : the location of the working directory you want to use
-v : verbose output
--with-coverage : use the coverage plugin, which tells you how much of your code has been run (and therefore tested)
--cover-package : the package to which coverage should be applied
--cover-html : generate HTML output showing coverage results
--cover-html-dir : specify the directory in which HTML coverage output should be placed
tokenize-coverage : the directory for HTML coverage output

For other options, see http://nose.readthedocs.org/en/latest/usage.html


Be sure to document and write new unit tests for any modifications made to the package.

Notes:
    [1] Each test class usually begins with Test*, with a capital T
    [2] Each test is prefixed with test_*
    [3] Ensure that the module directories are in the PYTHONPATH; e.g.,
        export PYTHONPATH=$PYTHONPATH:/home/{user}/Coding/Projects/nlp:/home/{user}/Coding/Projects/nlp/tokenizer:/home/{user}/Coding/Projects/nlp/naive

        where {user} is your username (based on a Linux distribution; your path may differ)

"""

# Import various nose tools for testing:
from nose.tools import eq_, raises # ability to check for equality or whether an error occurs (raises an exception)

# Import the module we want to test: tokenize
from tokenizer import *

# Tests:
class TestTokenize:
    """Test cases for the Tokenizer"""

    def setUp(self):
        """For each test, run some initialization code; e.g., initialize a class instance
        """
        self._tokenizer = Tokenizer()

    def tearDown(self):
        """After each test, run some completion code; e.g., remove an initialized class instance
        """
        del self._tokenizer

    # HTML tags:
    def test_removeTags(self):
        """tokenizer should remove HTML tags"""
        tag = '&lt;html class="my-class"&gt; text &lt;/html&gt;'
        tokens = self._tokenizer.tokenize(tag)
        eq_(tokens[0][0], unicode('text'))

    # Split Sentences:
    def test_splitSentences(self):
        """tokenizer should split sentences"""

        text = 'This is my first sentence. This is my second sentence? This is my third sentence! This is a sentence with a "quote."'

        _output = [
            ['This', 'is', 'my', 'first', 'sentence'],
            ['.'],
            ['This', 'is', 'my', 'second', 'sentence'],
            ['?'],
            ['This', 'is', 'my', 'third', 'sentence'],
            ['!'],
            ['This', 'is', 'a', 'sentence', 'with', 'a', '"', 'quote'],
            ['.', '"'],
            []
        ]

        for i in range(0, len(_output)):
            sentence = _output[i]
            for j in range(0, len(sentence)):
                token = sentence[j]
                _output[i][j] = unicode(token)

        output = self._tokenizer.tokenize(text)
        eq_(_output, output)



class TestPrivateMethods:
    """Test cases for private methods in the Tokenizer class"""

    def setUp(self):
        """For each test, run some initialization code; e.g., initialize a class instance
        """
        self._tokenizer = Tokenizer()

    def tearDown(self):
        """After each test, run some completion code; e.g., remove an initialized class instance
        """
        del self._tokenizer

    # Convert a string to unicode:
    def test_unicode_converts_string(self):
        """unicode conversion should convert string to unicode"""
        s = 'text'
        _s = self._tokenizer._unicode(s)
        eq_(unicode(s), _s)

    def test_unicode_should_gracefully_handle_improper_encodings(self):
        """unicode conversion should gracefully handle improper encodings"""
        self._tokenizer._unicode('\x81')

    # Convert HTML to unicode:
    def test_html2unicode_converts_entities(self):
        """html2unicode conversion should convert properly formed HTML entities to unicode"""
        tag = '&lt;html&gt;'
        eq_(self._tokenizer._html2unicode(tag), unicode('<html>'))

    def test_html2unicode_alpha_numeric_equivalents(self):
        """html2unicode conversion should return the same unicode for alpha and numeric encodings"""
        tag = '&copy;'
        _tag = '&#169;'
        eq_(self._tokenizer._html2unicode(tag), self._tokenizer._html2unicode(_tag))

    def test_html2unicode_should_gracefully_handle_improper_encodings(self):
        """html2unicode conversion should gracefully handle improper encodings"""
        tag = '&#999999999;' # integer too large
        eq_(self._tokenizer._html2unicode(tag), unicode(tag))

    def test_html2unicode_should_gracefully_handle_unknown_entities(self):
        """html2unicode conversion should gracefully handle unknown entities"""
        tag = '&thisismymadeupentity;' # integer too large
        eq_(self._tokenizer._html2unicode(tag), unicode(tag))

class TestOutputToFile:
    """Test token output to file"""

    def setUp(self):
        """For each test, run some initialization code; e.g., initialize a class instance
        """
        self._tokenizer = Tokenizer()

    def tearDown(self):
        """After each test, run some completion code; e.g., remove an initialized class instance
        """
        del self._tokenizer

    def test_write_to_file(self):
        """Test whether tokens have been written to file"""

        filename = "test.txt"
        output = [['Hello', 'Denise'], ['!']]
        data = [[unicode('Hello'), unicode('Denise')], [unicode('!')]]


        self._tokenizer.filename  = filename
        self._tokenizer._saveToFile(data)

        try:
            with open(filename, 'wb') as f:
                pickle.dump(data, f)

            with open(filename, 'rb') as f:
                _output = pickle.load(f)

            eq_(_output, output)

        except:
            raise








