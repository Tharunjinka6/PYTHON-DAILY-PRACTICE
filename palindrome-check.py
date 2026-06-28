class Solution:
    def isPalindrome(self, n):
		# code here
		n=abs(n)
		original=n
		d=len(str(n))
		k=""
		for i in range(d):
		    temp=n%10
		    n=n//10
		    k=str(k)+str(temp)
		reversed_digit=int(k)
		if original==reversed_digit:
		    return True
		else:
		    return False
		    