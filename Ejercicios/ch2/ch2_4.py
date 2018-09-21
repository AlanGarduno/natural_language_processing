from nltk.corpus import swadesh


es2en = swadesh.entries(['es','en']) #Se establece los idiomas con los cuales se trabajara
l = ['cenizas','nieve', 'hincharse'] #parabras a traducirse
traslate = dict(es2en) # se inicializa un diccionario(Tabla hash) en donde se buscaran las palabras
for i in l:
    print(traslate[i]) #Se itera sobre la lista que contiene las palabras 