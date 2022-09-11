f = open('abc.txt')

data = f.readlines()

count = 0
for l in data:
    if count == 5:
        break
    print(l)
    count += 1