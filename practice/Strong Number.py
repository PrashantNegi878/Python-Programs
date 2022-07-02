def findStrong(n):
    total=0
    for i in range(len(n)):
        sum=1
        for j in range(1,int(n[i])+1):
            sum=sum*j
        total+=sum
    if total==int(n):
        return 1
    else:
        return 0

a=input("Enter 1st no = ")
a1=findStrong(a)
if a1==1:
    print("Strong Number")
else:
    print("Not a Strong Number")