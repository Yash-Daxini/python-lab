n = int(input("Enter size of list:"))

a = []

for i in range(0,n):
    a.append(int(input("Enter element:")))

a.reverse()

for i in a:
    print(i,sep="",end=" ")