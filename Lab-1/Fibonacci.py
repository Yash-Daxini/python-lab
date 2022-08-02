n = int(input("Enter n:"))

a = 0
b = 1
# c = 0
print(a)
print(b)
for i in range(3,n+1):
    c = a + b
    temp = b
    b = c
    a = temp
    print(c)

