import nltk
from nltk.corpus import brown
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token)

print()

sent = '''
 The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
 other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
 Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
 said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
 accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
 interest/NN of/IN both/ABX governments/NNS ''/'' ./.
 '''
tagged_token_list = [nltk.tag.str2tuple(t) for t in sent.split()]
print(tagged_token_list)

print()


brown_news_tagged = brown.tagged_words(categories='news')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.keys()
tag_fd.plot(cumulative = True)

