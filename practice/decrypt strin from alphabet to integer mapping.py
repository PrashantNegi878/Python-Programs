a={}
temp2=106
for i in range(1,10):
    a[str(i)]=chr(96+i)

for i in range(10,27):
    a[str(i)+"#"] = chr(temp2)
    temp2=temp2+1
# print(a)
code="1326#"
msg=""
i=0
while i <len(code):
    if i+2<len(code) and code[i+2]=="#":
        s=code[i:i+3]
        msg=msg+a[s]
        i=i+3
    else:
        msg=msg+a[code[i]]
        i=i+1
print(msg)
