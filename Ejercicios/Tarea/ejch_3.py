import nltk

def opne_file(fname):
    f=open(fname, 'r', encoding='utf-8')
    text=f.read()
    f.close()
    return text

text = opne_file('e960401.html')
tokens = nltk.word_tokenize(text)
nltk_text = nltk.Text(tokens)
print(nltk_text.collocations())

