n = int(input("Enter Size Of the List:"))
a = []
for i in range(0,n):
    a.append(int(input("Enter element:")))

b = a[int(n/2):n]
c = a[0:int(n/2)]

a.clear()

a.extend(b)
a.extend(c)

print(a)