def reverseDLL(head):
    while head is not None:
        nxt = head.next
        head.next = head.prev
        head.prev = nxt
        if nxt is not None:
            head = nxt
        else:
            break

    return head