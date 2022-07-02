def merge(arr1, n, arr2,m):
    for i in range(0, m):
        arr1.append(arr2[i])
    arr2.clear()
    arr1.sort()
    for a in arr1:
        print(a)
    for a in arr2:
        print(a)

arr1=[9,6,2,5,1,3]
arr2=[1,5,7,8,9,2]
merge(arr1,6,arr2,6)