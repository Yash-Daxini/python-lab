from re import S


n = int(input("Enter n:"))

sum = 0
for i in range(1,n+1):
    sum += i*i*i

print(sum)