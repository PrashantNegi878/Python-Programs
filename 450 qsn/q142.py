def isCircular(head):
    first = head
    flag = 0
    head = head.next
    while head is not None:
        if head.next == first.next:
            flag = 1
            break
        head = head.next
    if flag == 1:
        return 1
    else:
        return 0
