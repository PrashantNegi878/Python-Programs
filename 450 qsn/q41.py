class Solution:

	def rowWithMax1s(self,arr, n, m):
		l1=len(arr)
		l2=len(arr[0])
		count=0
		max=0
		row=-1
		for i in range (l1):
		    count=0
		    for j in range (l2):
		        if arr[i][j]==1:
		            count+=1
		    if count>max:
		        max=count
		        row=i
		return row