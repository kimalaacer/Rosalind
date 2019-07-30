# http://rosalind.info/problems/hamm/
# this is a solution for the rosalind problem to calculate the number of point mutations in DNA.
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).
data = open('rosalind_hamm.txt')

string = {}
string[0] = data.readline()[:-1]
string[1] = data.readline()

hamming_distance = 0

for n in range(len(string[0])):
    if string[0][n] == string[1][n]:
        pass
    else:
        hamming_distance += 1

print (hamming_distance)
