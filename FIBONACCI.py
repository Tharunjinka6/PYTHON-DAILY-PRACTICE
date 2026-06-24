class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n==0:
            return 0
        if n==1:
            return 1
        a,b=0,1
        f=0
        if n>=2:
            for i in range(2,n+1):
                f=a+b
                a=b
                b=f
        return f