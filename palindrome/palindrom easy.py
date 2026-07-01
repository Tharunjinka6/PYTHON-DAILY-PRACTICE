class Solution:
    def isPalindrome(self, n):
		# code here
		if n==0:
		    return True
		n1=abs(n)
		n2=''
		m=n1
		while n1>0:
		    b=n1%10
		    n2=n2+str(b)
		    n1=n1//10
	    result=int(n2)
	    if m==result:
	        return True
	    else:
	        return False
