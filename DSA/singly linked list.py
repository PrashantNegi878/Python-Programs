class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        newnode = Node(data)
        newnode.ref=self.head
        # print("Added element",data)
        self.head=newnode

    def add_end(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
            # print("Added element", data)

    def add_after(self,data,x):
        if self.head is None:
            print("Empty Linked List")
            return
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n.data==x:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode

    def add_before(self,data,x):
        if self.head is None:
            print("Empty Linked List")
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref.data != x:
            print("Element not found")
        else:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode

    def add_empty(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
        else:
            print("Linked List is not Empty")

    def delete_start(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        elif self.head.ref is None:
            self.head = None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def delete_node(self,x):
        if self.head is None:
            print("Empty Linked List")
            return
        if self.head.data==x:
            self.head=self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Element not found")
        else:
            n.ref = n.ref.ref


    def print_ll(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref


ll1=LinkedList()
ll1.add_begin(10)
ll1.add_begin(7)
ll1.add_begin(20)
ll1.add_end(30)
ll1.add_begin(5)
ll1.add_end(40)
ll1.add_end(50)
ll1.add_after(41,40)
ll1.add_before(39,40)
ll1.delete_start()
ll1.delete_end()
ll1.delete_node(41)
ll1.print_ll()
ll1.add_empty(10)




