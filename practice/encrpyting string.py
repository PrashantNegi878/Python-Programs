s="wwxyzwww"
s_new=""
s_last=""
dictionary ={}
count=1
for i in range (1,10):
    dictionary[chr(96+i)]=str(i)
for i in range (10,27):
    dictionary[chr(96+i)]=str(i)+"#"
for i in range(1,10):
    dictionary[str(i)]=f"({str(i)})"
# print(dictionary)
s=s+"-"
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        s_new+=s[i-1]
        if count>1:
            s_new += str(count)
        count=1
for i in range (len(s_new)):
        s_last+=dictionary[s_new[i]]
print(s_last)


