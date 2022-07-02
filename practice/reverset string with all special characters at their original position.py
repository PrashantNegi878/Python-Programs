s="a-bC-dEf-ghIj"
a=[]
newstr=""
for i in range(len(s)-1,-1,-1):
    if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
        a.append(s[i])

for i in range(len(s)):
    if (ord(s[i])<65) or (ord(s[i])>122) or (ord(s[i])>90 and ord(s[i])<97):
        a.insert(i,s[i])
        # print(ord(s[i]),s[i])
for i in a:
    newstr=newstr+i
print(newstr)

