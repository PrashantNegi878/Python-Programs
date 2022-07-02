def intersetPoint(head1, head2):
    flag = 0
    head2temp = head2
    while head1 is not None:
        head2 = head2temp
        while head2 is not None:
            if head1.next == head2.next:
                flag = 1
                break
            head2 = head2.next
        if flag == 1:
            break
        head1 = head1.next
    if flag == 1:
        value = head1.next.data
    else:
        value = -1

    return value