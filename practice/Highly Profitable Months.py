n=8
arr=[5,3,5,7,8]
k=3
count=0
total=0
for i in range (1,len(arr)):
    if arr[i]>arr[i-1]:
        count+=1
    else:
        if count>(k-1):
            total+=(count-(k-1))
        count=1
    if i==len(arr)-1:
        if count > (k - 1):
            total += (count - (k - 1))
print(total)
