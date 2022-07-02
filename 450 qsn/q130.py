class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        l1=[]
        flag=0
        temphead=head
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
            head.next=None
        return temphead
