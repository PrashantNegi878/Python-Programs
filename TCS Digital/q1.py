n=int(input())
tot=0
chk=1
def findfactors(num):
    arr=[]
    i=9
    while i>1:
        if num%i==0:
            arr.append(i)
            num=num/i
            i+=1
        i-=1
    return arr

if n<10:
    num=n+10
    print(num)
else:
    arr=findfactors(n)
    if len(arr)==0 :
        print("-1")
    else:
        # print(arr)
        for i in range(len(arr)-1,-1,-1):
            tot=tot*10+arr[i]
            chk*=arr[i]
        # print(arr)
        if chk==n:
            print(tot)
        else:
            print(-1)
