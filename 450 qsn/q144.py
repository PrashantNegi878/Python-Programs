class Solution:
    def isPalindrome(self, head):
        temphead=head
        l=[]
        flag=0
        while head is not None:
            l.append(head.data)
            head=head.next
        for i in range(len(l)//2):
            if l[i]!=l[len(l)-1-i]:
                flag=1
                break
        if flag==1:
            return 0
        else:
            return 1