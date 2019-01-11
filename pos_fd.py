import nltk

from nltk import FreqDist

import pandas as pd

f = open("Test_TextFile.txt")
file1 = f.read()

words = nltk.tokenize.word_tokenize(file1)
tag_words = nltk.pos_tag(words)
#print(tag_words)

nouns = []
for words, pos in tag_words:
    if pos in ['NN', 'NNS', 'NNP', 'NNPS']:
        nouns.append(words)
nouns.sort()

fDist = FreqDist(nouns)

fDistpd = pd.DataFrame(fDist, index=[0])

print(fDistpd)

f.close()






