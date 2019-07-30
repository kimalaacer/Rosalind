from Bio.Align.Applications import MuscleCommandline
cline = MuscleCommandline(input="opuntia.fasta", out="opuntia.txt")
print(cline)
muscle -in opuntia.fasta -out opuntia.txt
