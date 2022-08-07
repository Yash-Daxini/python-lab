n = int(input("Enter Size Of the List:"))
a = []

large = 0
for i in range(0,n):
    a.append(int(input("Enter element:")))
    if large < a[i]:
        large = a[i]

print("Largest Element : ",large)