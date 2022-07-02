class Solution:

    def findallsum(self, root, height):
        if not root:
            return 0, height - 1
        l = r = []
        l = self.findallsum(root.left, height + 1)
        r = self.findallsum(root.right, height + 1)
        if l[1] == r[1]:
            return root.data + max(l[0], r[0]), l[1]
        h = max(l[1], r[1])
        if h == l[1]:
            s = l[0]
        else:
            s = r[0]
        return root.data + s, h

    def sumOfLongRootToLeafPath(self, root):
        # arr=[]
        height = 0
        s, h = self.findallsum(root, height)
        # print(h,s)
        return s