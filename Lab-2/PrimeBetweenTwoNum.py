def PrimeBetween(n1,n2):
    flag = True
    for i in range(n1,n2+1):
        flag = True
        for j in range(2,i):
            if i % j == 0:
                flag = False
        if flag :
            if i != 1:
                print(i)



n1 = int(input("Enter First Number :"))
n2 = int(input("Enter Second Number :"))

PrimeBetween(n1,n2)
