a=[0,4,-2,8,6,-3,7,9,-9]
n=len(a)
j=0
temp=0
for i in range(0,n):
    if a[i]<0:
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
        j+=1
print (a)
