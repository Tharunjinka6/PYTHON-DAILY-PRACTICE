class Solution:
	def reverseDigits(self, n):
		# Code here
		d=len(str(n))
		k=""
		for i in range(d):
		    temp=n%10
		    n=n//10
		    k=str(k)+str(temp)
		reversed_digit=int(k)
		return reversed_digit