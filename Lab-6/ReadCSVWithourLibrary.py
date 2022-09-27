f = open('E:\\Y\\DIET\\Sem-5\\PDS\\Labs\\MultiIndexDemo.csv')

data = f.readlines()

flag = True

for line in data:
    if flag:
        flag = False
        continue

    l = line.split(',')
    print(l[0] , end=" ")
    print(l[1] , end=" ")
    print(l[2] , end=" ")
    print()

    