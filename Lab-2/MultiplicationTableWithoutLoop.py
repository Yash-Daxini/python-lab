import re


def MultiTable(n,i):
    return n*i


n = int(input("Enter n :"))

for i in range(1,11):
    print(MultiTable(n,i))

