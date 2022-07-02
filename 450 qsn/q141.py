class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temphead = head
        tot = 0
        while head is not None:
            tot += 1
            head = head.next
        tot = tot // 2
        head = temphead
        while tot > 0:
            head = head.next
            tot -= 1
        return head
