str = input("Enter String:")
start = 0
for i in range(0,len(str)):
    if(str[i] == " " or (i == len(str)-1)):
        if i == len(str)-1:
            end = i+1
        else:    
            end = i
            
        if not(end-start&1):
            print(str[start:end+1])
        start = i+1

