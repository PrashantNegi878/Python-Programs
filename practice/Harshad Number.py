def findHarshad(n):
    sum=0
    for i in range (len(n)):
        sum=sum+int(n[i])
    if int(n)%sum==0:
        return 1
    else:
        return 0

a=input("Enter 1st no = ")
a1=findHarshad(a)
if a1==1:
    print("Harshad Number")
else:
    print("Not an Harshad Number")