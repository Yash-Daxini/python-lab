def Sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i*i

    print(sum)



n = int(input("Enter n:"))

Sum(n)
