k = int(input("Enter value of k:"))

a = [(1,2,3),(4,6,8),(1,2,3),(4,5,6)]

for i in a:
    flag = True
    for j in i:
        if j % k != 0:
            flag = False
    if flag:
        print(i)