n = int(input("Enter size of list:"))

a = []

for i in range(0,n):
    a.append(int(input("Enter element:")))

a.sort()

if n&1 :
    print(a[int(n/2)])
else:
    print((a[int(n/2) - 1] + a[int(n/2)])/2)