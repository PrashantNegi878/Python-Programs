class Solution:

    def checkLeft(self, root, arr):
        if not (root):
            return
        if root.left:
            arr.append(root.data)
            self.checkLeft(root.left, arr)
        elif root.right:
            arr.append(root.data)
            self.checkLeft(root.right, arr)

    def checkLeaf(self, root, arr):
        if not (root):
            return
        if root.left:
            self.checkLeaf(root.left, arr)
        if not (root.left) and not (root.right):
            arr.append(root.data)
        if root.right:
            self.checkLeaf(root.right, arr)
        return

    def checkRight(self, root, arr):
        if not (root):
            return
        if root.right:
            self.checkRight(root.right, arr)
            arr.append(root.data)
        elif root.left:
            self.checkRight(root.left, arr)
            arr.append(root.data)

    def printBoundaryView(self, root):
        arr = []
        arr.append(root.data)
        self.checkLeft(root.left, arr)
        # print(arr)
        self.checkLeaf(root, arr)
        # print(arr)
        self.checkRight(root.right, arr)
        # print(arr)
        return arr