s="a1c1e1"
i=0
strr=""
def shift(i,j):
    j=chr(ord(i)+int(j))
    return(i+j)

while i+1<len(s):
    temp=shift(s[i],s[i+1])
    strr=strr+temp
    i+=2
print(strr)


