class Solution:
    # The given root is the root of the Binary Tree

    # Return the root of the generated BST
    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)

    def change(self, root, arr, z):
        if not root:
            return
        self.change(root.left, arr, z)
        root.data = arr[z[0]]
        z[0] += 1
        self.change(root.right, arr, z)

    def binaryTreeToBST(self, root):
        arr = []
        z = [0]
        self.inorder(root, arr)
        arr.sort()
        self.change(root, arr, z)
        return root