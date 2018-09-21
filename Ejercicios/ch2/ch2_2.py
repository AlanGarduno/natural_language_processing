import nltk
from nltk.corpus import brown

news_text = brown.words(categories='romance')
#Desoliegue de propiedades de un corpus en particular, en este caso brown
#print('Numero de categorias: ', str(len(brown.categories())))
#print('Numero de archivos: ',  str(len(brown.fileids())))
#print('Numero de caracteres: ',str(len(brown.raw('cr09'))))
#print('Numero de palabras: ', str(len(brown.words('cr09'))))
#print('Numero de oraciones: ', str(len(brown.sents('cr09'))))


#Conteo de conicidencias
#fdist =  nltk.FreqDist([w.lower() for w in news_text]) #texto
#modals = ['love', 'hate'] #Palabras a contar frecuencia
#for m in modals:
#    print(m + ':', fdist[m]) #Buscamos y mostramos la frecuencia

#Conteo de conincidencias en diferentes categorias
cdf = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

genres = ['news','romance', 'humor'] #Generos donde se buscara
words = ['hate','love'] #Palabras a buscar en genero

cdf.tabulate(conditios=genres, samples=words)
cdf.plot()
