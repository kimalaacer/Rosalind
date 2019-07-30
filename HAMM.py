# http://rosalind.info/problems/hamm/
# this is a solution for the rosalind problem to calculate the number of point mutations in DNA.
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).



file=open('rosalind_hamm.txt','r')
s1=file.readline().strip()
s2=file.readline().strip()

hamming_distance=0
for i in range(len(s1)):
    if s1[i]==s2[i]:
        hamming_distance=hamming_distance
    else:
        hamming_distance=hamming_distance+1
print(hamming_distance)
