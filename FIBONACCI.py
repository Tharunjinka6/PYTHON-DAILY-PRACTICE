class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        a,b=0,1
        f=0
        if n>=2:
            for i in range(n-1):
                f=a+b
                a=b
                b=f
        return f