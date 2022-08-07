from asyncio.windows_events import NULL
from itertools import count


n = (int(input("Enter Size Of the List:")))

a = []
for i in range(0,n):
    a.append((input("Enter element:")))

word = (input("Enter Word:"))
k = int(input("Enter k:"))

if a.count(word) < k:
    print("Not Available ",k," times")
else :
    index = 0
    count = 1
    while count != k:
        index = a.index(word,index+1)
        count += 1

    a.pop(index)

    for i in a:
        print(i,sep=" ",end=" ")
    