def swap (a,b):
    return b,a

arr=[1,12,6,8,4,2,3,9,5]
l=len(arr)
count=0
for i in range(l):
    for j in range(l-1-i):
        count+=1
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=swap(arr[j],arr[j+1])
    print(arr)

print(count)

