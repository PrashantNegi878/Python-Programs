class Solution:
    def addOne(self,head):
        current=head
        sum=0
        temp=0
        while current is not None:
            # temp=current.data
            sum=sum*10+current.data
            current=current.next
        sum=sum+1
        head.data=sum
        head.next=None
        return head