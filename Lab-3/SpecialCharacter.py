str = input("Enter String:")

count = 0

if str.find("@") != -1 or str.find("&") != -1 or str.find("$") != -1 or str.find("#") != -1:
    print("yes")
else:
    print("No")
