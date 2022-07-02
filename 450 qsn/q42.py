class Solution:
    def sortedMatrix(self,N,Mat):
        # Mat[0].sort()
        a=[]
        b=[[]]
        element=0
        for i in range(N):
            for j in range(N):
                a.append(Mat[i][j])
        a.sort()
        # print(len(a))
        for i in range(N):
            for j in range(N):
                Mat[i][j]=a[element]
                element+=1
        return Mat