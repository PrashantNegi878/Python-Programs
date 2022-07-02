def LevelOrder(root, arr, low, high):
    if not root:
        return
    LevelOrder(root.left, arr, low, high)
    LevelOrder(root.right, arr, low, high)
    if root.data >= low and root.data <= high:
        arr.append(root.data)


def getCount(root, low, high):
    arr = []
    LevelOrder(root, arr, low, high)
    return len(arr)