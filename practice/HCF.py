a=int(input("Enter no.1 = "))
b=int(input("Enter no.2 = "))
m=min(a,b)
arr=0
for i in range(2,m+1):
    if a%i==0 and b%i==0:
        arr=i
print(arr)