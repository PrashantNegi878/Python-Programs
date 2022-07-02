class Solution:

    def makestring(self, root, dic):
        if not root:
            return "."
        if not root.left and not root.right:
            return str(root.data)
        l = self.makestring(root.left, dic)
        r = self.makestring(root.right, dic)
        st = str(root.data) + l + r
        if st not in dic:
            dic[st] = 1
        else:
            dic[st] += 1
        return st

    def dupSub(self, root):
        dic = {}
        # str=""
        self.makestring(root, dic)
        # print(dic)
        # for i in dic:
        #     print(i)
        for i in dic:
            if len(i) >= 2 and dic[i] > 1:
                return 1
        return 0
