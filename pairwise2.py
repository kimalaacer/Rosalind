from Bio import pairwise2
from Bio.pairwise2 import format_alignment
for a in pairwise2.align.globalms("ACCGT", "ACG", 2, -1, -10, -1):
   print(format_alignment(*a))
