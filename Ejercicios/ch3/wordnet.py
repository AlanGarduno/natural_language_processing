import nltk
from nltk.corpus import wordnet as wn

print(wn.synsets('computer')) #Sinominos en computadora
print(wn.synset('computer.n.01').lemma_names() ) #Sinonimos que e encuatrasn 

computer = wn.synset('computer.n.01')

types_of_computers = computer.hyponyms()
computer_meronyms = computer.part_meronyms()
print('Hiponimos computadora: ',types_of_computers)
print('Meronimos computadora: ',computer_meronyms)
print()
auto = wn.synset('car.n.01')
print('Meronimos de carro: ', auto.part_meronyms())
print()
bird = wn.synset('bird.n.01')
print('Holonimos bird: ',bird.member_holonyms())
