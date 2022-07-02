class Solution:

    def chk(self, root, arr):
        if not root:
            return
        self.chk(root.left, arr)
        arr.append(root.data)
        self.chk(root.right, arr)

    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        arr = []
        self.chk(root, arr)
        for i in range(0, len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return 0
        return 1