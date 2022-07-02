class bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if data==self.key:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild= bst(data)

    def search(self,data):
        if self.key is None:
            print("Tree is Empty\nNothing to Search")
            return
        if self.key==data:
            print("Node is Found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("None is not present in Tree")
        else:
            if self.rchild :
                self.rchild.search(data)
            else:
                print("None is not present in Tree")

    def preorder(self):
        if self.key is None:
            print("Tree is empty\nNothing to Print")
            return
        print(self.key,end=" -> ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()


    def inorder(self):
        if self.key is None:
            print("Tree is Empty\nNothing to Print")
            return
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" -> ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.key is None:
            print("Tree is Empty\nNothing to Print")
            return
        if self.lchild:
            self.lchild.inorder()
        if self.rchild:
            self.rchild.inorder()
        print(self.key, end=" -> ")

    def delete(self,data):
        if self.key is None:
            print("Tree is Empty\nNothing to Delete")
            return
        if data <self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("Node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("Node is not present in the tree")
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self

    def min_node(self):
        if self.key is None:
            print("Empty Tree\nCant find Min")
            return
        current=self
        while current.lchild:
            current=current.lchild
        print("\nSmallest Node  : ",current.key)

    def max_node(self):
        if self.key is None:
            print("Empty Tree\nCant find Min")
            return
        current=self
        while current.rchild:
            current=current.rchild
        print("\nLargest Node  : ",current.key)










# root=bst(10)
# root.lchild=5
# print(root.key)
# print(root.lchild)
# print(root.rchild)
l1=[10,6,3,1,22,12,6,98,3,7]
root=bst(None)

for i in l1:
    root.insert(i)

# root.search(10)
root.delete(10)
print("preorder")
root.preorder()
print("\ninorder")
root.inorder()
print("\npstorder")
root.postorder()

root.max_node()
root.min_node()