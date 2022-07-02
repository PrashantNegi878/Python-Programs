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

    def rotate(self,head,k):
        prev=None
        next=head.ref
        while head is not None and k>0:
            head.nref=prev
            prev=head
            head=next
            next=next.ref





DLL1= Doublyll()
l1=[1,2,3,4,5,6,7,8,9]
for i in l1:
    DLL1.add_end(i)
DLL1.rotate(DLL1.head,4)



# rough work for another qsn
# def display(arr,len):
#     i=len
#     if len==-1:
#         return 1
#     elif arr[i]<5:
#         print(f"{arr[i]} suqare =",arr[i]*arr[i])
#     display(arr,len-1)
#
#
#
# arr=[3,6,8,2,1,9]
# display(arr,len(arr)-1);



