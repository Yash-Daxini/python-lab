from itertools import count


f = open('abc.txt')

words = f.read().split()

inputword = input("Enter Word Whose Occurrences You want to count : ")
count = 0
for word in words:
    if word == inputword:
        count += 1

print("Occurrences Of '",inputword,"': " , count)