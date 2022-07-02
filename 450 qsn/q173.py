def findtopview(self, root, w, h, arr):
    if root == None:
        return
    if w not in arr:
        arr[w] = [root.data, h]
    elif arr[w][1] > h:
        arr[w] = [root.data, h]
    self.findtopview(root.left, w - 1, h + 1, arr)
    self.findtopview(root.right, w + 1, h + 1, arr)
    return


# Function to return a list of nodes visible from the top view
# from left to right in Binary Tree.
def topView(self, root):
    w = 0
    h = 0
    arr = {}
    a2 = []
    self.findtopview(root, w, h, arr)
    for i in sorted(arr):
        a2.append(arr[i][0])
    return a2