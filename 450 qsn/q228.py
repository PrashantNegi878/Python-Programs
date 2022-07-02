price= [ 7,10,4 ]
money=45
count=1
arr=[]
total=0
temp=0
for i in price:
    arr.append([i,count])
    count+=1
arr.sort()
print(arr)
for i in range(len(arr)):
    temp=0
    temp=min(arr[i][1],int(money/arr[i][0]))
    print(arr[i][0],temp)
    money=money-(temp*arr[i][0])
    total=total+temp
print(total)
