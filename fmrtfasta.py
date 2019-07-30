from Bio import Entrez
Entrez.email = "XXXXXXX@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["NM_013179"], rettype="fasta")
records = handle.read()
print records
