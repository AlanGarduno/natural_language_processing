import clean_tokens
import nltk

data = clean_tokens.get_text_string('e960401.html')
sents = nltk.sent_tokenize(data)

espefici = sents[12]
print(espefici)
tokens_espec = nltk.word_tokenize(espefici)
print(tokens_espec)
print(nltk.pos_tag(tokens_espec))
