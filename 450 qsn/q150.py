class Node:
    def __init__(self,data):
        self.pref=None
        self.data=data
        self.nref=None


class Doublyll:
    def __init__(self):
        self.head=None

    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked List is not Empty\nCannot Insert Element")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref = new_node
            new_node.pref=n

    def add_after(self,data,x):
        if self.head is None:
            print("Linked List is Empty\nCannot Find and Add Element")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("Element not Found")
            else:
                new_node=Node(data)
                new_node.nref = n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is Empty\nCannot Find and Add Element")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("Element Not Found")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is Empty \nCannot Delete Element")
        elif self.head.nref is None:
            self.head = None
            print("Linked List is Empty \nAfter Deletion")
        else:
            self.head=self.head.nref
            self.head.pref=None

    def delete_end(self):
        if self.head is None:
            print("Linked List is Empty \nCannot Delete Element")
            return
        if self.head.nref is None:
            self.head=None
            print("Linked List is Empty \nAfter Deletion")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n=n.pref
            n.nref=None

    def delete_by_value(self,x):
        if self.head is None:
            print("Linked List is Empty \nCannot Delete Element")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head=None
            else:
                print("Element not Found \nCannot Delete Element")
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if n.data==x:
                break
            n=n.nref
        if n.nref is not None:
            n.pref.nref=n.nref
            n.nref.pref=n.pref
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print("Element not Found \nCannot Delete Element")



    def prindll(self):
        if self.head is None:
            print("Linked List is Empty \nNothing to Print")
        else:
            n=self.head
            while n is not None:
                print(" -->",n.data,end="")
                n=n.nref

    def prindll_reverse(self):
        if self.head is None:
            print("Linked List is Empty \nNothing to Print")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data," <-- ",end="")
                n=n.pref
    def rotate(self,head,k):
        last=head
        head2=head
        while last.nref is not None:
            last=last.nref
        while k >0:
            last.nref=head
            head.pref=last
            last=last.nref
            head=head.nref
            head.pref=None
            last.nref=None
            k-=1
        print("")
        while head is not None:
            print(head.data,end=" -> ")
            head=head.nref






DLL1= Doublyll()
l1=[1,4,7,2,3,6,5,9,8]
for i in l1:
    DLL1.add_end(i)
DLL1.prindll()
DLL1.rotate(DLL1.head,3)
# DLL1.insert_empty(20)
# DLL1.add_begin(10)
# DLL1.add_end(30)
# DLL1.add_after(25,20)
# DLL1.add_after(26,30)
# DLL1.add_before(15,20)
# DLL1.add_before(5,10)
# DLL1.delete_begin()
# DLL1.delete_end()
# DLL1.delete_by_value(0)
