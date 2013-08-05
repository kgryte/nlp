#!/usr/bin/env python
# coding: utf-8

# Doc String: used for help
"""A naive sentiment analysis implementation"""

# Module version number:
__version__ = '0.1.0'

# Required modules:
import sys
import os
import json
import pandas as pd

# Define exceptions; we first define a base class which inherits from 'exception' and then derive any further errors from this base class. This is so we can name the errors and provide any tailored error handling:
class NaiveSentimentError(Exception):
    """Base class for errors in the naive sentiment analysis module"""

    pass

# Define the naive sentiment class:
class NaiveSentiment(object): # inherit from the base object
    """Class for Naive Sentiment instances


    """

    def __init__(self):
        """Initialize instance properties"""





