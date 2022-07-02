def getNthFromLast(head,n):
    temphead=head
    length=0
    while head is not None:
        head=head.next
        length+=1
    head=temphead
    if n>length:
        return -1
    n=length-n
    while n>0:
        head=head.next
        n-=1
    return head.data