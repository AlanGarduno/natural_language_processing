from write import writeDict

def raw_freq_vectors(fname_vocabulary, fname_contexts):
    f_vocabulary=open(fname_vocabulary, encoding='utf-8')
    voc=f_vocabulary.read()
    vocabulary=voc.split()
    f_vocabulary.close()
    
    f_contexts=open(fname_contexts, encoding='utf-8')
    contexts=f_contexts.readlines()
    f_contexts.close()
    
    raw_freq_vectors_dict={}
    for context in contexts:
        words=context.split()
        vector=[]
        for voc in vocabulary:
            vector.append(words[1:].count(voc))
        raw_freq_vectors_dict[words[0]]=vector
        print('raw_frequency_vectors function ', str(contexts.index(context)))
    
    return raw_freq_vectors_dict
    
'''test if run as application'''
if __name__=='__main__':
    fname_vocabulary='e960401_vocabulary.txt'    
    fname_contexts='e960401_contexts.txt'
    raw_freq_vectors_dict=raw_freq_vectors(fname_vocabulary, fname_contexts)
    #writeDict(raw_freq_vectors_dict, 'e960401_raw_freq.txt')
    
   