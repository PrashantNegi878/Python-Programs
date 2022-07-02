class Solution:
    def compute(self, head):
        prev = None
        n = head.next
        while n is not None:
            head.next = prev
            prev = head
            head = n
            n = n.next
        head.next = prev

        largest = head.data
        check = head.next
        prev = head
        temphead = head
        while check is not None:
            if check.data < largest:
                prev.next = check.next
            else:
                largest = check.data
                prev = check
            check = check.next

        prev = None
        head = temphead
        n = head.next
        while n is not None:
            head.next = prev
            prev = head
            head = n
            n = n.next
        head.next = prev

        return head