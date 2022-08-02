from sys import flags


n = int(input("Enter n:"))

flag = True
for i in range(2,n):
    if n%i == 0:
        flag = False
if flag:
    print("Prime")
else :
    print("Not Prime")
        
