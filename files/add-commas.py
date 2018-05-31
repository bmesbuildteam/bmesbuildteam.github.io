f = open("test.csv", 'r')
o = open("out.txt", 'w')

for c in f.read():
    if (c != '\n'):
        o.write(c)
    else:
        o.write(',')
