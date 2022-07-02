class Solution:

    def finddiameter(self, root, mx):
        if root == None:
            return 0
        l = self.finddiameter(root.left, mx)
        r = self.finddiameter(root.right, mx)
        mx[0] = max(mx[0], l + r + 1)
        return max(l, r) + 1

    # Function to return the diameter of a Binary Tree.
    def diameter(self, root):
        mx = [0]
        self.finddiameter(root, mx)
        return mx[0]