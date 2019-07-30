from Bio.Seq import Seq
my_file_name = "rosalind_prot.txt"
my_file = open(my_file_name)
my_file_contents = my_file.read()
seq = Seq(my_file_contents)

print seq.translate()
