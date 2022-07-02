def diameter(self, root):
    if root == None:
        return 0
    if root.left:
        l = self.diameter(root.left)
    if root.right:
        r = self.diameter(root.right)
    return l + r + 1