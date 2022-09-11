f = open('abc.txt')

data = f.read()

max = ""
for word in data.split(' '):
    if len(word.strip()) > len(max.strip()) :
        max = word.strip()
print(max)