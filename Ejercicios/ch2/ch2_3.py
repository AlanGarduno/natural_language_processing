import nltk
import os
from nltk.corpus import PlaintextCorpusReader

corpus_root = str(os.getcwd()+'/Corpus/') #Directorio del corpus
file_list = PlaintextCorpusReader(corpus_root,'.*') #Lee todos los archivos de la carpeta 
#print(file_list.fileids())
#print(len(word_list.fileids())) #Imprime el total de archivos
print(file_list.sents(fileids='e960401.html')[19]) #Obtiene las oraciones con el file
