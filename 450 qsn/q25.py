a=[3,1,2,3,2,2,1,4,3,3]
k=3
c=[]
b=list(set(a))
# print(b)

for i in range(len(b)):
    count=0
    for j in range(len(a)):
        if b[i]==a[j]:
            count+=1
    c.append(count)
# print(c)
for i in range(len(b)):
    if c[i]>(len(a)//k):
        print(b[i])
