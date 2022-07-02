s1="The quick brown fox jumped over the lazy dog"
a1=s1.split()
count=0
s2=""
for i in range(len(a1)):
    if a1[i][0].lower()=="a" or a1[i][0].lower()=="e" or a1[i][0].lower()=="i" or a1[i][0].lower()=="o" or a1[i][0].lower()=="u":
        a1[i]=a1[i]+"ma"
    else:
        a1[i]=a1[i][1:len(a1[i])]+a1[i][0]
        a1[i] = a1[i] + "ma"
    count+=1
    for j in range(count):
        a1[i]=a1[i]+"a"

for i in range(len(a1)):
    s2=s2+a1[i]+" "
print(s2)
