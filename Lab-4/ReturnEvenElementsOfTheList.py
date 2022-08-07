
n = int(input("Enter size of Array:"))

a = []

for i in range(0,n):
    print("Enter ",(i+1)," Element:" , end=" ")
    a.append(int(input()))

print([i for i in a if not(i&1)])

