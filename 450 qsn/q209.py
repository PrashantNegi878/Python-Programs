class Solution:

    def levelorder(self, root, arr):
        if not root:
            return
        self.levelorder(root.left, arr)
        arr.append(root.data)
        self.levelorder(root.right, arr)

    def kthLargest(self, root, k):
        arr = []
        self.levelorder(root, arr)
        return arr[-k]