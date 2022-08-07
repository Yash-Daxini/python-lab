str = input("Enter String:")
temp = ""
for i in str:
    if str.count(i) > 1:
        if temp.count(i) == 0:
            temp += i
            temp += " "

print(temp)