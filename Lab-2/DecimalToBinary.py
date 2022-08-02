def DeciToBi(n):
    b = []
    while n != 0:
        b.append(n%2)
        n = int(n/2)

    b.reverse()
    for i in b:
        print(i,end=" ")




n = int(input("Enter n : "))

DeciToBi(n)

