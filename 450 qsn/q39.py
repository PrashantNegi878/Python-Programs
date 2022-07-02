class Solution(object):
    def searchMatrix(self, matrix, target):
        temp=0
        clen=len(matrix)
        rlen=len(matrix[0])
        for i in range(clen):
            for j in range (rlen):
                if matrix[i][j]==target:
                    temp+=1
                    print(i,j)
        if temp==0:
            return 0
        else:
            return 1