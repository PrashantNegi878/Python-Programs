class Solution:

    def findlca(self, root, n1, n2):
        if not root:
            return None
        if root.data == n1 or root.data == n2:
            return root
        l = self.findlca(root.left, n1, n2)
        r = self.findlca(root.right, n1, n2)
        if l != None and r != None:
            return root
        if l == None and r == None:
            return None
        if l != None:
            return l
        if r != None:
            return r

    def dist(self, root, val):
        if not root:
            return 0
        if root.data == val:
            return 1
        l = self.dist(root.left, val)
        r = self.dist(root.right, val)
        if not l and not r:
            return 0
        elif l == 0:
            return r + 1
        else:
            return l + 1

    # def dist(self,root,val,dist):
    #     if not root:
    #         return 0
    #     if root.data==val:
    #         return dist
    #     l=self.dist(root.left,val,dist+1)
    #     r=self.dist(root.right,val,dist+1)
    #     if not l and not r:
    #         return 0
    #     else:
    #         return max(l,r)

    def findDist(self, root, a, b):

        aa = self.findlca(root, a, b)
        # if aa==None:
        #     root.data=-1
        #     return root
        l = self.dist(aa, a)
        r = self.dist(aa, b)
        return (l + r) - 2