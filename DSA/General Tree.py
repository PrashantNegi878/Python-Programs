class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def addChild(self,child):
        child.parent=self
        self.children.append(child)


def build_product_tree():
    root =TreeNode("Electronics")
    laptop=TreeNode("Laptop")
    root.addChild(laptop)


build_product_tree()

