

def get_lemmas_dic( fname ):
#    dic_lemmas ={}
    f = open(fname,'r')
    data = f.readlines()
    f.close()
    for i in range(len(data)):
        aux = data[i].split()
        



def get_lemma(word, lemmas, dic_lemmas):
    for n in lemmas:
        if word == n:
           lemma = dic_lemmas[word]
    return lemma


def main():
    get_lemmas_dic('test.txt')

if __name__ == '__main__':
    main()