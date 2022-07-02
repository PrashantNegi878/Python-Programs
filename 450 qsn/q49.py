class Solution:
	def isPlaindrome(self, S):
		a=len(S)
		count=0
		for i in range(0,a//2):
		    if S[i]!=S[a-1-i]:
		        count+=1
		if count>0:
		    return 0
		else:
		    return 1