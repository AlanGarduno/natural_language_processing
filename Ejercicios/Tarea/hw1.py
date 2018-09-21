import nltk
import os
import sys
import string
import re
from bs4 import BeautifulSoup
from nltk.corpus import PlaintextCorpusReader
from pprint import pprint
import clean_tokens_from_dash

BASE_DIR = os.getcwd() + '/Corpus/'

def read_file(name):
    f = open(BASE_DIR+name+'.html',encoding='UTF-8')
    text = f.read()
    f.close()
    return text

def clean_text(text):
    soup = BeautifulSoup(text,'lxml')
    text_clean = soup.get_text()
    text_clean = text_clean.replace('\x97', ' ') #Quitando Caracteres problematicos
    text_clean = text_clean.replace('\ufffd', ' ') #Quitando caracteres problematicos
    text_clean = text_clean.lower()
    return text_clean

def create_clean_file(text_clean, name):
    f = open('clean_data_'+name+'.txt','w',encoding='UTF-8')
    f.write(text_clean)
    f.close()

def get_clean_raw_data(text_clean):
    return text_clean

def read_clean_data(name):
    f = open('clean_data_'+name+'.txt','r',encoding='UTF-8')
    data = f.read()
    f.close()
    return data

def write_clean_tokens_in_file(tokens,fname):
    f = open(fname,'w',encoding='UTF-8')
    for i in range(len(tokens)):
        w = tokens[i]
        f.write(str(w))
    f.close()

def clean_tokens(tokens):
    cleaned_tokens = []
    for tok in tokens:
        t = []
        for char in tok:
            if re.match(r'[a-záéíóúñüA-ZÁÉÍÓÚÑ]',char):
                t.append(char)
        letter_token = ''.join(t)
        if letter_token != '':
            cleaned_tokens.append(letter_token)
    return cleaned_tokens

def get_word_context(word,tokens, window_size):
    context = []
    for i in range(len(tokens)):
        if tokens[i] == word:
            for j in range(i-1, i+(int(window_size/2)-1),-1):
                if j >= 0:
                    context.append(tokens[j])
            try:
                for j in range(i+1,i+(int(window_size/2)+1)):
                    context.append(tokens[j])
            except IndexError:
                pass
    return context 


def get_vocabulary(tokens):
    vocabulary = sorted(set(tokens))
    return vocabulary

def tokennize_clean_data(name):
    data = read_clean_data(name)
    data = nltk.Text(nltk.sent_tokenize(data))
    filtered_data = clean_tokens(data)
    #print(type(filtered_data))
    #pprint(filtered_data)
    string_data = ''.join(filtered_data)
    tokens = nltk.Text(nltk.word_tokenize(string_data)) #Separa en Tokens los datos
    return tokens
    #print(tokens)
    #print(len(tokens))
    #vocabulary = sorted(set(tokens)) #Obtenemos los tokens unicos
    #print(len(vocabulary))
    #print(vocabulary[:3000])
    #clean_tokens = [filter(None,[remove_characters_after_tokenization(tokens)
    #                                                       for tokens in sentence_tokens])
    #                                                       for sentence_tokens in tokens]
    #list(clean_tokens)                                                         
    #pprint(clean_tokens)
    """
    tokens = sorted(set(text.words('clean_data_'+name+'.txt'))) #Obtiene la lista de tokes unicos
    print('Unique Tokens in text: '+str(len(tokens)))
    repeated_tokens = text.words('clean_data_'+name+'.txt') #Obtiene una lista de tokens repetidos
    print('Repeated Tokens in text: '+str(len(repeated_tokens)))
    text = nltk.Text(repeated_tokens) #Convierte a un objeto manipulable de nltk
    print('Similar words:')   
    text.similar('empresa')"""

    
def main():
    if int(sys.argv[1]) == 0:
        text = read_file(sys.argv[2])
        print('Cleaning the text...')
        try:
            text_clean = clean_text(text)
        except FileNotFoundError:
            print('Something goes wrong... :(')
        print('Text cleaned...')
        create_clean_file(text_clean,sys.argv[2])
    else:
        tokens = tokennize_clean_data(sys.argv[2])
        context1 = get_word_context('empresa',tokens,8)
        context2 = get_word_context('compañia',tokens,8)
        context3 = get_word_context('agua',tokens,8)
        print(context1)
        print(context2)
        print(context3)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        print('Missing arguments... [option] [file_name]')
        sys.exit()
