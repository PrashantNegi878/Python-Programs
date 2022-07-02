class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def findlca(self, root, n1, n2):
        if not root:
            return None
        if root.data == n1 or root.data == n2:
            return root
        l = self.findlca(root.left, n1, n2)
        r = self.findlca(root.right, n1, n2)
        if l != None and r != None:
            return root
        if l != None:
            return l
        if r != None:
            return r

    def lca(self, root, n1, n2):
        # Code here
        # arr=[]
        a = self.findlca(root, n1, n2)
        if a == None:
            root.data = -1
            return root
        return a