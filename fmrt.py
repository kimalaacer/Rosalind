from Bio import Entrez
from Bio import SeqIO
Entrez.email = "merouehchady@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["NM_001079732, JX295575, NM_002133, JX205496, NM_001081821, NM_001172751, NM_002037, NM_001135551"], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))
print len(records[0].seq); print len(records[1].seq); print len(records[2].seq); print len(records[3].seq); print len(records[4].seq); print len(records[5].seq); print len(records[6].seq); print len(records[7].seq); print len(records[8].seq)
