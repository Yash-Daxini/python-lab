a = input("Enter String:")
flag = True
for i in range(0,len(a)):
    if(a[i] != a[len(a)-i-1]):
        flag = False

if flag:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")