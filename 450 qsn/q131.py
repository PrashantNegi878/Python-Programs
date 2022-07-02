# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     #  to add node at beginning
#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node
#
#     #  to add node at the end
#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_node
#
#     #   to add node after an element
#     def add_after(self, data, x):
#         n = self.head
#         while n is not None:
#             if n.data == x:
#                 break
#             n = n.ref
#         if n is None:
#             print("Element not found")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node
#
#     #   to add node before an element
#     def add_before(self, data, x):
#         if self.head is None:
#             print("Linked List is Empty")
#             return
#         if self.head.data == x:
#             new_node = Node(data)
#             new_node.ref = self.head
#             self.head = new_node
#             return
#         n = self.head
#         while n.ref is not None:
#             if n.ref.data == x:
#                 break
#             n = n.ref
#
#         if n.ref is None:
#             print("Element not found in the Linked List")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node
#
#     #  to add node only if linked list is empty
#     def add_empty(self,data):
#         if self.head is None:
#             new_node=Node(data)
#             self.head=new_node
#         else:
#             print("Linked List is not Empty")
#
#     #  to print the linked list
#     def print_ll(self):
#         if self.head is None:
#             print("Linked list is empty !")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref
#
#
# ll1 = LinkedList()
# ll1.add_end(20)
# ll1.add_begin(15)
# ll1.add_end(40)
# ll1.add_end(80)
# ll1.add_begin(10)
# ll1.add_after(16, 15)
# ll1.add_before(15.5, 16)
# ll1.print_ll()
# ll1.add_empty(12)



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
        k=0
        if self.head is None:
            print("Empty Linked List")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" -> ")
                n=n.ref
                if k>10:
                    break
                k+=1

    def makeloop(self,head):
        k=0
        temp=None
        while head.ref is not None:
            head=head.ref
            k+=1
            if k==2:
                temp=head.ref
        head.ref=temp

    def findloop(self, head):
        l1=[]
        while head is not None:
            for i in l1:
                if i==head.ref:
                    print("")
                    print(f"Starting Point = {head.ref.data}")
                    head.ref=None
                    break
            if head.ref is None:
                break
            l1.append(head.ref)
            head=head.ref




ll1=LinkedList()
l1=[1,2,3,4,5,6,7,8]
for i in l1:
    ll1.add_end(i)
ll1.print_ll()
print("\n")
ll1.makeloop(ll1.head)
ll1.print_ll()
ll1.findloop(ll1.head)
print("\n")
ll1.print_ll()
# ll1.add_begin(10)
# ll1.add_begin(7)
# ll1.add_begin(20)
# ll1.add_end(30)
# ll1.add_begin(5)
# ll1.add_end(40)
# ll1.add_end(50)
# ll1.add_after(41,40)
# ll1.add_before(39,40)
# ll1.delete_start()
# ll1.delete_end()
# ll1.delete_node(41)
# ll1.print_ll()
# ll1.add_empty(10)
