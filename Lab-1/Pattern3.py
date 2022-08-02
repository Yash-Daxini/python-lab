n = int(input("Enter n:"))

a = 0
for i in range(0,int(n/2)+1):

    for k in range(0,i):
        print(end="    ")

    for j in range(n-2*i,0,-1):
        print(" # ",end=" ")
    print()

for i in range(int(n/2)-1,-1,-1):

    for k in range(i,0,-1):
        print(end="    ")

    for j in range(n-2*i,0,-1):
        print(" # ",end=" ")
    print()