import nltk, re, pprint
from urllib import request

url = 'http://www.gutenberg.org/files/2554/2554.txt'

raw = request.urlopen(url).read()
type(raw)
len(raw)
tokens = nltk.word_tokenize(raw)
type(tokens)
len(tokens)
text = nltk.Text(tokens)
type(text)
text.collocations()
raw.find('PART I')
raw.find('End of Project Gutenberg\'s Crime')

