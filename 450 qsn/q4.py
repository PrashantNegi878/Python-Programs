a=[1,2,1,1,0,0,2,1,0]
n=len(a)
zero=0
one=0
two=0
print(a)
for i in a:
        if i==0:
            zero+=1
        if i==1:
            one+=1
for i in range(0,zero):
    a[i]=0
for i in range(zero,zero+one):
    a[i]=1
for i in range(zero+one,n):
    a[i]=2
print (a)
