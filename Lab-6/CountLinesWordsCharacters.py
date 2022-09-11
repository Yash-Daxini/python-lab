from itertools import count


f = open('abc.txt')

data = f.readlines()

f.close()

print("Number of Lines : ",len(data) )

f1 = open('abc.txt')
data1 = f1.read()

# print(len(data1))

print("Number of Words : ",len(data1.split(' ')))

print("Number of Characters : ",len(data1))

