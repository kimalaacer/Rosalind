# test

i = 1
f = open('testfilesforcounting.txt', 'r')
for line in f.readlines():
    if i % 2 == 0 :
        print line
    i += 1
