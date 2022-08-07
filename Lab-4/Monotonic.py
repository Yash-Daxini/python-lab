
n = int(input("Enter size of list:"))

a = []

for i in range(0,n):
    a.append(int(input("Enter element:")))

if(a[0]<=a[1]):
    flag = True
    for i in range(0,n-1):
        if(a[i] <= a[i+1]):
            pass
        else:
            flag = False
            print("Not Monotonic")
            break
    if flag:
        print("Monotonic")

else:
    flag = True
    for i in range(0,n-1):
        if(a[i] >= a[i+1]):
            pass
        else:
            flag = False
            print("Not Monotonic")
            break
    if flag:
        print("Monotonic")
