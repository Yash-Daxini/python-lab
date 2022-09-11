from itertools import count
from tokenize import String


def isPrime(n):
    if n == 2:
        return False
    count = 0
    for i in range(2,n):
        if n % i == 0:
            return False
    return True    

with open('primenumbers.txt','w') as f:
    for i in range(1,50):
        if isPrime(i):
            f.write(str(i)+" ")