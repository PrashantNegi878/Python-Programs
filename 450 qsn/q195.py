def findancs(root, k, arr):
    if not root:
        return
    l = findancs(root.left, k, arr)
    r = findancs(root.right, k, arr)
    if l != None or r != None or root.data == k:
        arr.append(root.data)
        return root.data
    else:
        return
    # if l or r:
    #     arr.append(root.data)
    # if :
    #     arr.append(k)
    # return root.data


def kthAncestor(root, k, node):
    arr = []
    a = findancs(root, node, arr)
    # print(k)
    # print(arr)
    if k < len(arr):
        return arr[k]
    else:
        return -1
    # return arr[0]