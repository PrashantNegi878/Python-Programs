
class Solution:
    def median(self, matrix, r, c):
    	matrix.sort()
    	l1=len(matrix)
    	l2=len(matrix[0])
    	m2=[]
    	for i in range(l1):
    	    for j in range (l2):
    	        m2.append(matrix[i][j])
    	m2.sort()
    	l3=len(m2)
    	return (m2[l3//2])