class Solution:

    # def Node(self,data):
    #     self.left=None
    #     self.data=data
    #     self.right=None

    # def inserttodll()

    def traversetree(self, root, arr):
        if not root:
            return
        self.traversetree(root.left, arr)
        arr.append(root)
        self.traversetree(root.right, arr)
        # return prev

    def bToDLL(self, root):
        arr = []
        head = Node(None)
        prev = Node(None)
        f = 0
        prev = self.traversetree(root, arr)
        # print(arr)
        for i in arr:
            if f == 0:
                f = 1
                head = i
                prev = i
            else:
                prev.right = i
                prev.right.left = prev
                prev = prev.right
        return head