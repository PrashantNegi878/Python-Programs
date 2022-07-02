def reverseLevelOrder(root):
    arr=[]
    a2=[]
    arr.append(root)
    while(len(arr)>0):
        a2.append(arr[0].data)
        if (arr[0].right):
            arr.append(arr[0].right)
        if (arr[0].left):
            arr.append(arr[0].left)
        arr.pop(0)
    a2.reverse()
    return a2