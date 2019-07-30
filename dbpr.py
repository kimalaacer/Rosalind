from Bio import ExPASy
from Bio import SwissProt
import operator
from functools import reduce
import re
handle = ExPASy.get_sprot_raw('Q9WAA1')
record = SwissProt.read(handle)
my_seq=record.cross_references
my_list=(list(reduce(operator.concat, my_seq)))
joinedlist=','.join(my_list)
my_GO=re.findall(r'P\:[\w ]+',joinedlist, re.M)
pattern = re.compile(r"P:")
result = [pattern.sub("", match) for match in my_GO]
print result[0]
print result[1]
print result[2]
