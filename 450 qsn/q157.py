class Solution:
    # Function to merge K sorted linked list.
    def mergeKLists(self, arr, K):
        # code here
        # return head of merged list
        l1 = []
        prev = None
        # print(arr[0].data)
        for i in arr:
            while i is not None:
                l1.append(i.data)
                prev = i
                i = i.next
        l1.sort()
        for i in l1:
            newList.add(i)

        return (prev.next)