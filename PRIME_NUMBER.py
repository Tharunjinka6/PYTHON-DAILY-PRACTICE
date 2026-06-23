class Solution:
    def isPrime(self, n):
        # code here
        if n>1:
            if n%1==0 and n%n==0:
                return True
            else:
                return False