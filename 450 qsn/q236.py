class Solution:
    def Maximize(self, a, n):
        sum=0
        a.sort()
        for i in range(len(a)):
            sum+=a[i]*i
        sum=sum%(1000000000+7)
        return(sum)