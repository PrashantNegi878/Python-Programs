def swap (a,b):
    return b,a

arr=[1,12,6,8,4,2,3,9,5]
l=len(arr)
count=0
for i in range(l-1):
    smallest=i
    for j in range(i,l):
        if arr[j]<arr[smallest]:
            smallest=j
    arr[i],arr[smallest]=swap(arr[i],arr[smallest])
print(arr)
# print(count)

