s = open ('rosalind_ini6.txt')
from collections import Counter
counts = Counter()
for sentence in s:
    counts.update(word.strip('.,?!"\'') for word in sentence.split())
print(counts)
