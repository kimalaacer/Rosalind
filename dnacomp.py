from Bio.Seq import Seq

seq = Seq("TCGGGCCC")

print seq.reverse_complement()
print seq.complement()
print seq.transcribe()
print seq.translate()
