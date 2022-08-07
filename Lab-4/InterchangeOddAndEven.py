n = int(input("Enter size of list:"))

a = []

for i in range(0,n):
    a.append(int(input("Enter element:")))

for i in range(0,n-1,2):
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp

for i in a:
    print(i , sep="",end=" ")