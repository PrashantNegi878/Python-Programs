dict = {
    0:1,
    1:1,
    2:2,
    3:3*2,
    4:4*3*2,
    5:5*4*3*2,
    6:6*5*4*3*2,
    7:7*6*5*4*3*2,
    8:8*7*6*5*4*3*2,
    9:9*8*7*6*5*4*3*2
}
arr=[]
n=int(input())
while n not in arr:
    sum=0
    arr.append(n)
    while n>=1:
        temp=n%10
        n=n//10
        sum+=dict[temp]
    n=sum
m=max(arr)
print(m*len(arr))