# to find Union of two arrays (count of no.s)
a=[1,4,9,8,5,3]
b=[1,2,3,4,4,9,8,5,3]
n=len(a)
m=len(b)
if n<m:
    small=a
    count=len(set(a))
    big=b
else:
    small=b
    count=len(set(b))
    big=a
    count=m
for i in set(big):
    flag=0
    for j in set(small):
        if i==j:
            flag=1
    if flag==0:
        count+=1
print (count)