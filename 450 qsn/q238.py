def maxSum(arr,n):
    arr.sort()
    arr2=[]
    sum=0
    for i in range(n//2):
        arr2.append(arr[i])
        arr2.append(arr[n-1-i])
    if n%2!=0:
        arr2.append(arr[(n//2)+1])
    # print(arr2)
    for i in range(n-1):
        sum+=abs(arr2[i]-arr2[i+1])
        # print(sum)
    sum+=abs(arr2[n-1]-arr2[0])
    return sum