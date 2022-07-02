class Solution:
    def maximizeSum(self, a, n, k):
        a.sort()
        # print(a)
        sum=0
        for i in range(n):
            if a[i]<0 and k>0:
                a[i]=-a[i]
                k-=1
            sum=sum+a[i]
        if k%2!=0:
            smallest=min(a)
            sum=sum-(2*smallest)
        return(sum) 