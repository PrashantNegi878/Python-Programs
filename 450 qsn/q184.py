class Solution:

    def retval(self, root, arr):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.data
        l = self.retval(root.left, arr)
        r = self.retval(root.right, arr)
        if l + r != root.data:
            arr[0] = 0
        root.data += l + r
        return root.data

    def isSumTree(self, root):
        arr = [1]
        self.retval(root, arr)
        return arr[0]