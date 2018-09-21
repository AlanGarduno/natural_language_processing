import nltk
import numpy as np
import clean_tokens_from_dash
import clean_tokens


def get_vacabulary(tokens):
    voc = sorted(set(tokens))
    return voc

def get_word_context(word,tokens,window_size):
    context=[] 
    for i in range(len(tokens)):
        if tokens[i] == word:
            for j in range(i-1, i-int(window_size/2)-1, -1): #left context
                if j >=0: 
                    context.append(tokens[j])
            try:
                for j in range(i+1, i+(int(window_size/2+1))): #right context
                    context.append(tokens[j])
            except IndexError:
                pass
    return context

def create_vectors(context,tokens):
    vector  = []
    for word in context:
        cont = 0
        for j in tokens:
            if word == j:
                cont += 1
        vector.append(cont)
    return vector

def get_cos_between_two_vectors(vector1, vector2):
    n_vector_1 = np.asarray(vector1)
    n_vector_2 = np.asarray(vector2)
    p_escalar = n_vector_1 @ n_vector_2
    magnitud = np.linalg.norm(n_vector_1) * np.linalg.norm(n_vector_1)
    cos = p_escalar/magnitud
    return cos 

def main():
    text_string = clean_tokens_from_dash.get_text_string('e960401.html')
    raw_tokens = clean_tokens_from_dash.get_raw_tokens(text_string)
    tokens_cleaned = clean_tokens.clean_tokens(raw_tokens)
    tokens_without_dahs = clean_tokens_from_dash.clean_tokens_from_initial_and_final_dash(tokens_cleaned)
    #final_tokens = clean_tokens_from_dash.clean_tokens_from_internal_dash(tokens_without_dahs)
    vocabulary = get_vacabulary(tokens_without_dahs)
    print('Vocabulary length', len(vocabulary))
    context1 = get_word_context('empresa',tokens_without_dahs,8)
    vector = create_vectors(context1,tokens_without_dahs)
    for word in tokens_without_dahs:
        context = get_word_context(word,tokens_without_dahs,8)
        vector2 = create_vectors(context,tokens_without_dahs)
        print(word, get_cos_between_two_vectors(vector,vector2))

if __name__ == '__main__':
    main()