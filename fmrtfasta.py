from Bio import Entrez
Entrez.email = "merouehchady@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["NM_013179"], rettype="fasta")
records = handle.read()
print records
