def Patt4(n):
    a = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(a,end=" ")
            a += 1
        print()


n = int(input("Enter n:"))

Patt4(n)
