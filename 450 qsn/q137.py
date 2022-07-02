def findIntersection(head1,head2):
    temphead1=head1
    temphead2=head2
    ll3=linkedList()
    while head1 is not None:
        head2=temphead2
        while head2 is not None:
            if head1.data==head2.data:
                ll3.insert(head1.data)
                head2=temphead2
                break
            head2=head2.next
        head1=head1.next
    return (ll3.head) 