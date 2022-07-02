class Solution:
	def find_median(self, v):
		length=len(v)
		v.sort()
		if length==1:
		    return v[0]
		elif length==2:
		    return (v[0]+v[1])//2
		if length%2==0:
		    return ((v[length//2-1]+v[length//2])//2)
        else:
            return v[length//2]