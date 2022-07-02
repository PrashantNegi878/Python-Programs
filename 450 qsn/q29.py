class Solution:
    def trappingWater(self, arr,n):
        left=[]
        right=[]
        l=0
        r=0
        sum=0
        for i in range (n):
            if arr[i]>l:
                l=arr[i]
            left.append(l)
        for i in range (n-1,-1,-1):
            if arr[i]>r:
                r=arr[i]
            right.append(r)
        right.reverse()
        # print(left)
        # print(arr)
        # print(right)
        for i in range(n):
            sum+=min(left[i],right[i])-arr[i]
        return sum