class Solution:
    def reverse(self, head, k):
        current = head
        prev = None
        next = current
        a = 0
        if k == 1:
            return head
        while current is not None and a < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            a += 1

        if current is not None:
            head.next = ob.reverse(current, k)
        return prev