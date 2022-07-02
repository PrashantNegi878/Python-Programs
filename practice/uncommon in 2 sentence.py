s1="apple apple"
s2="banana"
a1=s1.split()
a2=s2.split()
a3=[]
count=0
for i in a1:
    count=0
    for j in a2:
        if i==j:
            count+=1
    if count==0:
        if a1.count(i)>1:
            pass
        elif i not in a3:
            a3.append(i)
for i in a2:
    count=0
    for j in a1:
        if i==j:
            count+=1
    if count==0:
        if a2.count(i) > 1:
            pass
        elif i not in a3:
            a3.append(i)
print(a3)
