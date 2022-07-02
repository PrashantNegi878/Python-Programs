class Solution:
    # User function Template for python3

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        temp=0
        count=0
        a=arr.sort()
        for i in range(0,n-1):
            for j in range(i+1,n):
                if arr[j]<arr[i]:
                    count+=1
        return count