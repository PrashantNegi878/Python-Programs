class Solution:
    def toSumTree(self, root) :
        if not root:
            return 0
        l=self.toSumTree(root.left)
        r=self.toSumTree(root.right)
        temp=root.data
        root.data+=l+r
        if not(root.left) and not(root.right):
            temp=root.data
            # print(temp)
            root.data=0
            return root.data+temp
        root.data-=temp
        return root.data+temp