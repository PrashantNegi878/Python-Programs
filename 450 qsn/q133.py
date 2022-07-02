def removeDuplicates(head):
    current=head
    compnode=head
    prev=None
    while current is not None:
        while compnode is not None:
            if compnode.next is not None:
                if current.data==compnode.next.data:
                    compnode.next=compnode.next.next
                    continue
            compnode=compnode.next
        prev=current
        current=current.next
        compnode=current
    return head