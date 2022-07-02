def height(self, root):
    if root == None:
        return 0
    l = self.height(root.left)
    r = self.height(root.right)
    return max(l, r) + 1