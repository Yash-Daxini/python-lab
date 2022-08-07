a = []
b = []

for i in range(0,3):
    rows = []
    for j in range(0,3):
        print("Enter[",i+1,"] [",j+1,"]"," Element:",end=" ")
        rows.append(int(input()))
    a.append(rows)

for i in range(0,3):
    rows = []
    for j in range(0,3):
        print("Enter[",i+1,"] [",j+1,"]"," Element:",end=" ")
        rows.append(int(input()))
    b.append(rows)

temp = []

for i in range(0,3):
    for j in range(0,3):
        tempvar = 0
        for k in range(0,3):
            tempvar += a[i][k]*b[k][j]
        temp.append(tempvar)



for i in range(0,len(temp)):
        print(temp[i],end="  ")
        if((i+1)%3 == 0):
            print()
            