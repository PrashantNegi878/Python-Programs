class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def __str__(self,level=0):
        ret=" "*level+str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

    def addChild(self,Treenode):
        Treenode.parent=self
        self.children.append(Treenode)

tree=TreeNode("Drinks")
cold=TreeNode("Cold")
hot=TreeNode("Hot")
tree.addChild(cold)
tree.addChild(hot)
cofee=TreeNode("Cofee")
Tea=TreeNode("Tea")
hot.addChild(cofee)
hot.addChild(Tea)
Cola=TreeNode("Cola")
Shake=TreeNode("Shake")
cold.addChild(Cola)
cold.addChild(Shake)

print(tree)

# print(Shake.parent)