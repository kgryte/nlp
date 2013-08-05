#!/usr/bin/env python
# coding: utf-8

# Doc String:
"""
To run this script, ensure that you have set your PYTHONPATH:

export PYTHONPATH=$PYTHONPATH:/home/{user}/Coding/Projects/nlp:/home/{user}/Coding/Projects/nlp/tokenizer:/home/{user}/Coding/Projects/nlp/naive:/home/{user}/Coding/Projects/nlp/fileparser

where {user} is your username. Note that the above paths are for a linux system and according to my sub-directory convention. Yours will inevitably be different.

Once the paths are set, navigate to the 'nlp' directory in the Terminal and then

$python nlp.py

where the $ indicates the command prompt.

Currently, the output is simply printed to the terminal.


"""

# Package version number:
__version__ = '0.1.0'

# Required modules:
import fileparser as fp
import tokenizer as tk
import naive as nsa



# The url to parse:
url = 'http://www.bbc.co.uk/news/world-europe-23283684'

# Instantiate a new parser:
parser = fp.FileParser()

# Parse the url:
doc = parser.parse(url)

# Run the document through the tokenizer:
tokens = tk.Tokenizer().tokenize(doc)

print tokens


