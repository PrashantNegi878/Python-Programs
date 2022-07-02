
a = [-5, -2, 5, 2, 4, 7, -1, 8, 0, -8]
c=0
temp=0
for i in range(0,len(a)):
    temp=0
    if a[i]<0:
        temp=a[i]
        a[i]=a[c]
        a[c]=temp
        print(temp)
        print(c,a)
        c+=1
