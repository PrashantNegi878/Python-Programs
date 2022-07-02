class Solution:

    def chkbal(self, root, arr):
        if root == None:
            return 0
        l = self.chkbal(root.left, arr)
        r = self.chkbal(root.right, arr)
        # print(abs(l-r))
        if abs(l - r) > 1:
            arr[0] = True
            # print(flag)
        return max(l, r) + 1

    def isBalanced(self, root):
        arr = [False]
        ht = self.chkbal(root, arr)
        if arr[0] == False:
            return 1
        else:
            return 0