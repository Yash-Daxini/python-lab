n = int(input("Enter n:"))

sum = 0
for i in range(1,n+1):
    if i&1 == 0:
        if i == n:
            print(-i ," ", " = ")
        else:
            print(-i , " + ")
        sum += -i
    else :
        if i == n:
            print(-i , " = ")
        else:
            print(i , " + ")
        sum += i
    
print(sum)