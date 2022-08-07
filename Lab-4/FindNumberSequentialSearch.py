n = int(input("Enter size of list:"))

a = []

for i in range(0,n):
    a.append(int(input("Enter element:")))

num = int(input("Enter Number you want to search:"))
flag = False
for i in range(0,n):
    if num == a[i]:
        flag = True
        print(num," is at ",i+1," position")
        break

if not flag:
    print("Element Not Found")
