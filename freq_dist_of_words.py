import nltk

from nltk import FreqDist
import pandas as pd

f = open("Test_TextFile.txt")
file1 = f.read()
words = nltk.tokenize.word_tokenize(file1)
fDist = FreqDist(words)

fdist = pd.DataFrame(fDist, index=[0])
print(fdist)





