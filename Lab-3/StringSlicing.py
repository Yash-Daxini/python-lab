str = input("Enter String:")

k = int(input("Enter k :"))

a = str[0:k]
b = str[len(str)-k:len(str)]
temp = str

str = str.replace(a,"")

str += a

print("Left: ",str)

str = temp

str = str.replace(b,"")

str = "".join([b,str])

print("Right:",str)
