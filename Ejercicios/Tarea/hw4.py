import math
import nltk
import operator
import clean_tokens
import write

def conditional_entropy(pw1_1, pw2_1, pw1_1w2_1):
    pw2_0 = 1-pw2_1
    pw1_1w2_0 = pw1_1 - pw1_1w2_1
    pw1_0w2_0 = pw2_0 - pw1_1w2_0
    pw1_0w2_1 = pw2_1 - pw1_1w2_1
    if pw1_0w2_0 > 0 and pw1_1w2_0 > 0 and pw1_0w2_1 > 0 and pw1_1w2_1 > 0:
        condEntropy = (pw1_0w2_0 *math.log(pw2_0/pw1_0w2_0,2))+\
                        (pw1_1w2_0 *math.log(pw2_0/pw1_1w2_0,2))+\
                        (pw1_0w2_1 *math.log(pw2_1/pw1_0w2_1,2))+\
                        (pw1_0w2_1 *math.log(pw2_1/pw1_0w2_1,2))
    else:
        condEntropy = 0
    return condEntropy

def kldivergence(pw1_1, pw2_1, pw1_1w2_1):
    pw2_0 = 1-pw2_1
    pw1_1w2_0 = pw1_1 - pw1_1w2_1
    pw1_0w2_0 = pw2_0 - pw1_1w2_0
    pw1_0w2_1 = pw2_1 - pw1_1w2_1
    if pw1_0w2_0 > 0 and pw1_1w2_0 > 0 and pw1_0w2_1 > 0 and pw1_1w2_1 > 0:
        condEntropy = (pw1_0w2_0 *math.log(pw2_0/pw1_1*pw2_0,2))+\
                        (pw1_1w2_0 *math.log(pw2_0/pw1_1*pw2_0,2))+\
                        (pw1_0w2_1 *math.log(pw2_1/pw1_1*pw2_1,2))+\
                        (pw1_0w2_1 *math.log(pw2_1/pw1_1*pw2_1,2))
    else:
        condEntropy = 0
    return condEntropy

def get_sentences(text_string):
    sent_tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
    sentences = sent_tokenizer.tokenize(text_string)
    print('There are', len(sentences), 'sentences')
    return sentences

def delete_stopwords(tokens, fname):
    f = open(fname,'r', encoding='UTF-8')
    data = f.read()
    data = data.split('\n')
    for i in data:
        try:
            tokens.remove(i)
        except ValueError:
            pass
    return tokens


def main():
    fname = 'e960401.html'
    text_string = clean_tokens.get_text_string(fname)
    raw_tokens = clean_tokens.get_raw_tokens(text_string)
    clean_tokns = clean_tokens.get_clean_tokens(raw_tokens)
    fname_stopwords = 'stopwords_es.txt'
    tokens_without_stopwords = delete_stopwords(clean_tokns,fname_stopwords)

    vocabulary = clean_tokens.get_vocabulary(tokens_without_stopwords)
    sentences = get_sentences(text_string)
    N = len(sentences)

    pw2_1 = []
    for word in vocabulary:
        freq = 0
        for sent in sentences:
            if word in sent:
                freq += 1
        pw2_1.append(freq+0.25/N+1)

    W1 = 'empresa'
    for sent in sentences:
        if W1 in sent:
            freq +=1
    pw1_1 = (freq+0.25)/(N+1)

    pw1_1w2_1 = []
    for W2 in vocabulary:
        freq = 0
        for sent in sentences:
            if W1 in sent and W2 in sent:
                freq += 1
        pw1_1w2_1.append(freq+0.25/N+1)
    cond_entropy = {}

    for i in range(len(vocabulary)):
        #cond_ent = conditional_entropy(pw1_1, pw2_1[i], pw1_1w2_1[i]) primer metodo
        cond_ent = kldivergence(pw1_1,pw2_1[i], pw1_1w2_1[i])
        if cond_ent > 0:
            cond_entropy[vocabulary[i]] = cond_ent
        
    sorted_entropy = sorted(cond_entropy.items(), key = operator.itemgetter(1))
    write.writeList(sorted_entropy,'empresa_cond_entropy_2.txt')
        
            
if __name__ == '__main__':
    main()

