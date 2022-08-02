def Fibonacci(n):
    if(n == 1 or n == 0):
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


n = int(input("Enter n:"))

for i in range(0,n):
    print(Fibonacci(i))

