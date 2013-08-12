#!/usr/bin/env python
# coding: utf-8

"""Unit Tests:

To run these tests, use the following command in the Terminal from the parent directory (one-level above):

    $nosetests -w tests/ -v --with-coverage --cover-package naive --cover-html --cover-html-dir naive-coverage

*where the $ sign indicates the prompt and should not be included in the command.

-w : change the working directory
tests/ : the location of the working directory you want to use
-v : verbose output
--with-coverage : use the coverage plugin, which tells you how much of your code has been run (and therefore tested)
--cover-package : the package to which coverage should be applied
--cover-html : generate HTML output showing coverage results
--cover-html-dir : specify the directory in which HTML coverage output should be placed
naive-coverage : the directory for HTML coverage output


Be sure to document and write new unit tests for any modifications made to the package.
"""



# Import various nose tools for testing:
from nose.tools import eq_, raises

# Import the module we want to test: naive sentiment analysis
from naive import *

# Tests:
class TestNaive:
    """Test cases for naive sentiment analysis"""

    def setUp(self):
        """For each test, run some initialization code; e.g., initialize a class instance
        """
        pass

    def tearDown(self):
        """After each test, run some completion code; e.g., remove an initialized class instance
        """
        pass


