class Solution:

    def LevelOrder(self, root, arr):
        if not root:
            return
        self.LevelOrder(root.left, arr)
        arr[root.data] = 1
        self.LevelOrder(root.right, arr)

    def countPairs(self, root1, root2, x):
        dict1 = {}
        dict2 = {}
        tot = 0
        self.LevelOrder(root1, dict1)
        self.LevelOrder(root2, dict2)
        for i in dict1:
            if x - i in dict2:
                # print(i,x-i)
                tot += 1