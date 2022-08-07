x = int(input("Enter rows:"))
y = int(input("Enter column:"))

twod = []
row = []

for i in range(0,x):
    row = []
    for j in range(0,y):
        row.append((i+1)*(j+1))
    twod.append(row)
    
for i in range(0,x):
    for j in range(0,y):
        print(twod[i][j],end="   ")
    print()
