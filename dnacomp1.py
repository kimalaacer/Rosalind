from Bio.Seq import Seq
my_file_name = "rosalind_revc.txt"
my_file = open(my_file_name)
my_file_contents = my_file.read()
seq = Seq(my_file_contents)
print seq.reverse_complement()
print seq.complement()
print seq.transcribe()
print seq.translate()
