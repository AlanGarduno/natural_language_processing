import nltk

text = nltk.word_tokenize("And now for something completly diffrent")
print(nltk.pos_tag(text))

print()

text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
print(nltk.pos_tag(text))

print()

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print(text.similar('woman'))

print()

print(text.similar('bought'))

print()

print(text.similar('over'))

print()

print(text.similar('the'))