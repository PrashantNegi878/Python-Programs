class Solution:
    # Your task is to complete this function
    # function should return True/False or 1/0

    def retzeroone(self, root, arr, height):
        if not root:
            return
        if not root.left and not root.right:
            arr.append(height)
        self.retzeroone(root.left, arr, height + 1)
        self.retzeroone(root.right, arr, height + 1)

    def check(self, root):
        arr = []
        height = 0
        self.retzeroone(root, arr, height)
        # print(arr)
        if arr.count(arr[0]) == len(arr):
            return 1
        return 0