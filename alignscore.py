from Bio import Entrez
from Bio import SeqIO
Entrez.email = "merouehchady@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["JX308815.1, JX445144.1"], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))
seqa= records[0].seq
seqb= records[1].seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
for a in pairwise2.align.globalms(seqa, seqb, 5, -4, -10, -1):
   print(format_alignment(*a))
