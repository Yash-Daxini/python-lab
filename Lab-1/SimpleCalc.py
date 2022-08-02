from ast import operator


n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number:"))
op = (input("Enter Operation You Want To Perform:"))

if op == '+':
    print("Sum = ",(n1+n2))
elif op == '-':
    print("Subtraction = ",(n1-n2))
elif op == '*':
    print("Multiplication = ",(n1*n2))
elif op == '/':
    print("Division = ",(n1/n2))