def LeftView(root):
    arr=[]
    a2=[]
    if(root!= None):
        arr.append(root)
    temp=root
    n=len(arr)
    while len(arr)>0:
        temp=arr[0]
        a2.append(temp.data)
        n = len(arr)
        while n>0:
            temp = arr.pop(0);
            if temp.left!=None:
                arr.append(temp.left)
            if temp.right!=None:
                arr.append(temp.right)
            n-=1;
    return a2