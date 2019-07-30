from Bio import Entrez
Entrez.email = "merouehchady@gmail.com"
handle = Entrez.esearch(db="nucleotide", term='"Anthoxanthum"[Organism] AND "2003/7/25"[PDAT] : "2005/12/27"[PDAT]')
record = Entrez.read(handle)
record["Count"]
