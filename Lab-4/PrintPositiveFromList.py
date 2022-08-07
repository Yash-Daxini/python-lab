n = int(input("Enter size of list:"))

a = []

for i in range(0,n):
    a.append(int(input("Enter element:")))
    
for i in a:
    if i > 0:
        print(i,end=" ")