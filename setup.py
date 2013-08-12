from distutils.core import setup
import sys

sys.path.append('naive')
import naive

setup(name = 'sentiment analysis',
      version = '0.1.0',
      author = 'Denise Xifara',
      author_email = 'denisexifaras@googlemail.com',
      url = '',
      download_url = '',
      description = 'NLP and Sentiment Analysis',
      long_description = nlp.__doc__,
      package_dir = {'': 'nlp'},
      py_modules = ['naive'],
      provides = ['naive'],
      keywords = 'nlp sentiment',
      license = 'MIT',
      classifiers = ['Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python']
)