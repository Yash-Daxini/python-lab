
n = int(input("Enter n:"))

def is_prime(n):
    for i in range(2,int(n/2)):
        if n % i == 0 :
            return False
    return True



max = 0
for i in range(1,n+1):
    if n % i == 0:
        if(is_prime(i)):
            if max < i:
                max = i
print(max)
        
