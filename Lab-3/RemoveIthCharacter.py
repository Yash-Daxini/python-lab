str = input("Enter String:")
index = int(input("Enter index of character: "))
index -= 1
temp = ""

temp += str[0:index]
temp += str[index+1:len(str)]

str = temp
print(str)