import nltk
from nltk.corpus import cess_esp


cess_esp_tagged_sents = cess_esp.tagged_sents()
cess_esp_sents = cess_esp.sents()
unigram_tagger = nltk.UnigramTagger(cess_esp_tagged_sents)
print(unigram_tagger.tag(cess_esp_sents[12]))