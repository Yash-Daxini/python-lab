n = int(input("Enter Size Of the List:"))
a = []
for i in range(0,n):
    a.append(int(input("Enter element:")))

pos1 = int(input("Enter First Position:"))
pos2 = int(input("Enter First Position:"))

if( (pos1 >= 1 and pos1 <= n) or (pos2 >= 1 and pos2 <= n)):
    pos1 -= 1
    pos2 -= 1
    temp = a[pos1]
    a[pos1] = a[pos2]
    a[pos2] = temp
    for i in a:
        print(i,sep=" ",end=" ")

else:
    print("Invalid Position!")