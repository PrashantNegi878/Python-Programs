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
        if self.head is None:
            print("Empty Linked List")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.ref

    def find_pairs(self,head,k):
        l2 = []
        i=0
        temphead=head
        temphead2 = head
        temphead3 = head
        while temphead is not None:
            temphead2=head
            while temphead2 is not None:
                temphead3=head
                while temphead3 is not None:
                    if temphead.data+temphead2.data+temphead3.data==k:
                        if temphead.data not in l2 and temphead2.data not in l2:
                            l2.append(temphead.data)
                            l2.append(temphead2.data)
                            l2.append(temphead3.data)
                        break
                    temphead3=temphead3.ref
                temphead2=temphead2.ref
            temphead=temphead.ref
        print("")
        while i <len(l2):
            print(f"({l2[i]},{l2[i+1]},{l2[i+2]})")
            i+=3



ll1=LinkedList()
l1=[1,4,3,6,7,9,2,5]
for i in l1:
    ll1.add_end(i)
ll1.print_ll()
ll1.find_pairs(ll1.head,12)