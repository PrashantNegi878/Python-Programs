class Solution:
    # Function to store the zig zag order traversal of tree in a list.

    def zigZagTraversal(self, root):
        curr, queue = [], []
        temp = []
        temp.append(root)
        l = len(temp)
        flag = 1
        while temp:
            l = len(temp)
            while l != 0:
                if temp[0].left:
                    temp.append(temp[0].left)
                if temp[0].right:
                    temp.append(temp[0].right)
                curr.append((temp.pop(0)).data)
                l -= 1
            if flag == 1:
                for i in range(len(curr)):
                    queue.append(curr.pop(0))
                flag = 0
            elif flag == 0:
                for i in range(len(curr)):
                    queue.append(curr.pop(-1))
                flag = 1
        return queue