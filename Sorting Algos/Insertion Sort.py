arr=[8,1,4,9,2,3,6,5]
l=len(arr)
for i in range (1,l):
    temp=arr[i]
    j=i-1
    while j>=0 and arr[j]>temp:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
print(arr)
