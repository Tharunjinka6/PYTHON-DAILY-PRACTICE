class Solution:
    def sumOfDigits(self, n):
        # code here
        str_n=str(n)
        sum=0
        for i in str_n:
            sum=sum+int(i)
        return sum
    
    