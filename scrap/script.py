#!/usr/bin/env python

"""script.py

	- Use this script to perform naive sentiment analysis on text data.

	- To run:

		execfile('script.py')

	do so from the Python interpreter and make sure that you are in the same directory.
"""

#

import pandas as pd
import data as dat



# Use pandas to read in the sentiment lexicon:
df = pd.read_csv('lexicon/sentiment-lexicon.csv')

# If you want to preview:
#df.head()


# Load in the data using the data module:
data = dat.loadData()



# Look up words in the lexicon:
score = 0
word_count = 0
sentiment_tally = { 'neutral': 0, 'negative': 0, 'positive': 0 }
missing = {}
found = {}
for word in data:

	_score = 0

	# Get the lexicon row which matches our word:
	row = df[df.word1 == word]

	# Check if the word was found:
	if not row.shape[0]:
		# Store the missing word:
		if word in missing:
			missing[word] += 1
		else:
			missing[word] = 1
		# Move to next iteration:
		continue

	# Store the word in our found array:
	if word in found:
		found[word] += 1
	else:
		found[word] = 1

	# In the event that we return multiple entries for a particular word (e.g., when a word can be both a noun and an adjective ['will']), then we choose then first entry.
	row = row[:1]

	# Word was found:
	word_count = word_count + 1

	# Get the strength:
	strength = row.type

	if strength == 'weaksubj':
		_score = 1
	elif strength == 'strongsubj':
		_score = 2

	# Get the sentiment:
	sentiment = row.priorpolarity

	if sentiment == 'neutral':
		_score = _score * 0
		sentiment_tally['neutral'] += 1
	elif sentiment == 'positive':
		_score = _score * 1
		sentiment_tally['positive'] += 1
	elif sentiment == 'negative':
		_score = _score * -1
		sentiment_tally['negative'] += 1

	# Add this score to our total score:
	score = score + _score



# Calculate the average score:
score = score * 1.0 / word_count











