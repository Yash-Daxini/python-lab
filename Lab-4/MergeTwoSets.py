from typing import Set


n = int(input("Enter size of set:"))

a = set()
b = set()

print("\tEnter First Set")

for i in range(0,n):
    print("Enter ",i+1,"element:")
    a.add(input())

print("\tEnter Second Set")

for i in range(0,n):
    print("Enter ",i+1,"element:")
    b.add(input())

for i in b:
    a.add(i)

print(a)