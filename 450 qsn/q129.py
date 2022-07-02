class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        l1=[]
        flag=0
        l1.append(head)
        while head.next is not None:
            for i in l1:
                if head.next==i:
                    flag=1
                    break
            if flag==1:
                break
            l1.append(head.next)
            head=head.next
        if flag==1:
            return True
        else:
            return False