#!/usr/bin/env python
# coding: utf-8

# Doc String:
"""
To run this script, ensure that you have set your PYTHONPATH:

export PYTHONPATH=$PYTHONPATH:/home/{user}/Coding/Projects/nlp:/home/{user}/Coding/Projects/nlp/tokenizer:/home/{user}/Coding/Projects/nlp/naive:/home/{user}/Coding/Projects/nlp/fileparser

export PYTHONPATH=$PYTHONPATH:/Users/dionysiakiaraxifara/Documents/NLP/nlp:/Users/dionysiakiaraxifara/Documents/NLP/nlp/tokenizer:/Users/dionysiakiaraxifara/Documents/NLP/nlp/naive:/Users/dionysiakiaraxifara/Documents/NLP/nlp/fileparser

where {user} is your username. Note that the above paths are for a linux system and according to my sub-directory convention. Yours will inevitably be different.

Once the paths are set, navigate to the 'nlp' directory in the Terminal and then

$python nlp.py

where the $ indicates the command prompt.

Currently, the output is simply printed to the terminal.

-I needed to install: 
sudo easy_install pip
sudo easy_install beautifulsoup4
intalled Xcode from the Apple Store
Xcode - preferences - download - install command line tools
sudo easy_install pandas
sudo pip install lxml
sudo pip install html5lib
sudo pip install nose
sudo pip install coverage

"""

# Package version number:
__version__ = '0.1.0'

# Required modules:
import fileparser as fp
import tokenizer as tk
import naive as nsa
import pickle



# The url to parse:
url = 'http://www.bbc.co.uk/news/world-europe-23283684'

# Instantiate a new parser:
parser = fp.FileParser()

# Parse the url:
doc = parser.parse(url)

# Run the document through the tokenizer:
tokenizer = tk.Tokenizer() #initialize object
tokenizer.filename = 'test.txt' #cannot do tok.filename('test.txt') because here we're redefining an attribute (assigning a value)
tokenizer.tokenize(doc) #here we're calling a method which needs a parameter

#print tokens

with open('test.txt', 'rb') as f:
	thedata = pickle.load(f)

print(thedata)

#len(thedata)
#thedata[4][1:20]


#write out to file: use python's way to save unicode to string
#then read in file (which is an array of arrays) to do the SA


