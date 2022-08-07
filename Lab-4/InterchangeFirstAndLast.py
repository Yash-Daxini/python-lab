n = int(input("Enter Size Of the List:"))
a = []
for i in range(0,n):
    a.append(int(input("Enter element:")))

temp = a[0]
a[0] = a[n-1]
a[n-1] = temp

for i in a:
    print(i,sep=" ",end=" ")