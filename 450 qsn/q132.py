
def removeDuplicates(head):
    current=head
    while current.next is not None:
        if current.data==current.next.data:
            current.next=current.next.next
            continue
        current=current.next
    return head