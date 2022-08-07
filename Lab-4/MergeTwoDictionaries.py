n = int(input("Enter length of dictionary:"))

dict = {}
dict1 = {}

print("\tEnter Into First Dictionary")

for i in range(0,n):
    a = input("Enter Key:")
    b = input("Enter Value:")
    dict.update({a:b})

print("\tEnter Into Second Dictionary")

for i in range(0,n):
    a = input("Enter Key:")
    b = input("Enter Value:")
    dict1.update({a:b})


for key,value in dict1.items():
    dict.update({key:value})

print(dict)