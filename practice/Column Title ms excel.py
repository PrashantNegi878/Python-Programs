str="FXSHRXW"
i=0
total=0
for i in range (len(str)):
    j = 0
    temp = (ord(str[i]) - 64)
    for j in range(i,len(str)-1):
        temp=temp*26
        j+=1
    total=total+temp
print(total)