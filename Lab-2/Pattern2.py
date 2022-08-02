def Patt2(n):
    for i in range(0,n+1):
        for j in range(1,n+1-i):
            print(" $ ",end=" ")
        print()


n = int(input("Enter n:"))

Patt2(n)
