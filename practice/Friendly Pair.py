def findindex(n):
    sum=0
    for i in range(1,(n//2)+1):
        # print(i)
        if n%i==0:
            sum+=i
    return (sum//n)

a=int(input("Enter 1st no = "))
b=int(input("Enter 2nd No = "))
a1=findindex(a)
b1=findindex(b)
if a1==b1:
    print("Friendly Pair")
else:
    print("Not a Friendly Pair")
print(a1,b1)