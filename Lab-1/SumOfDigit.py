n = int(input("Enter number:"))

sum = 0
while n!=0:
    sum += n%10
    n = int(n / 10)

print(sum)