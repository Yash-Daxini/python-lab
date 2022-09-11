f = open('abc.txt')

data = f.read()

with open('xyz.txt','w') as f1:
    f1.write(data)