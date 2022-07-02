n=int(input("Enter any number = "))
sum=0
for i in range (1,n//2+1):
    if n%i==0:
        # print(i)
        sum+=i
if sum==n:
    print("PERFECT Number")
else:
    print("Not a PERFECT Number")