str = input("Enter String:")
word = input("Enter Word:")

sindex = str.index(word)
eindex = len(word)+sindex-1

rstr = ""
for i in range(eindex,sindex-1,-1):
    rstr += str[i]

str = str.replace(word,rstr)
print(str)