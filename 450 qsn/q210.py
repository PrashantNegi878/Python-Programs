class Solution:

    def levelorder(self, root, arr):
        if not root:
            return
        self.levelorder(root.left, arr)
        arr.append(root.data)
        self.levelorder(root.right, arr)

    # Return the Kth smallest element in the given BST
    def KthSmallestElement(self, root, K):
        arr = []
        self.levelorder(root, arr)
        if len(arr) >= K:
            return arr[K - 1]
        return -1