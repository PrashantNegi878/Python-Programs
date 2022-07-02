class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        sum1 = 0
        sum2 = 0
        len1 = 0
        prev = None
        first2 = first
        while first is not None:
            prev = first
            sum1 = sum1 * 10 + first.data
            first = first.next
            len1 += 1

        while second is not None:
            sum2 = sum2 * 10 + second.data
            second = second.next
        sum = sum1 + sum2
        s = []
        while sum > 0:
            s.append(sum % 10)
            sum = sum // 10

        for i in range(len(s) - 1, -1, -1):
            LL1.insert(s[i])

        first = prev.next
        return first
