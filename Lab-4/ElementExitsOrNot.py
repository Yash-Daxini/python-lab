n = int(input("Enter size of list:"))

a = []

for i in range(0,n):
    a.append(int(input("Enter element:")))

ele = int(input("Enter element which you have to check:"))

if a.count(ele) == 0:
    print(ele," Not Exits")
else:
    print(ele," Exits")