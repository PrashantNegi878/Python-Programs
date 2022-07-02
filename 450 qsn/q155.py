class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        temphead=head
        total=0
        zero=0
        one=0
        while head is not None:
            total+=1
            if head.data==0:
                zero+=1
            elif head.data==1:
                one+=1
            head=head.next
        # print (total,zero,one)
        head=temphead
        while head is not None:
            if zero>0:
                head.data=0
                zero-=1
            elif one>0:
                head.data=1
                one-=1
            else:
                head.data=2
            head=head.next
        return temphead