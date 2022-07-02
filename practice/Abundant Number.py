def findDivSum(n):
    sum=0
    for i in range(1,(n//2)+1):
        # print(i)
        if n%i==0:
            sum+=i
    return (sum)

a=int(input("Enter 1st no = "))
a1=findDivSum(a)
if a1>a:
    print("Abundant Number")
else:
    print("Not an Abundant Number")