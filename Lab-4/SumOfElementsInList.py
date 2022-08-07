from typing import List


n = int(input("Enter Size Of the List:"))
a = []
for i in range(0,n):
    a.append(int(input("Enter element:")))

sum = 0

for i in a:
    sum += i

print("Sum = ",sum)