from sys import flags


str = input("Enter String:")
flag = True

for i in str:
    if i == "1" or i == "0":
        pass
    else:
        print("NO")
        flag = False
        break

if flag:
    print("Yes")
