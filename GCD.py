#Time limit exceeded
class Solution:
    def gcd(self, a, b):
        # code here
        factors_a=[]
        factors_b=[]
        for i in range(1,a+1):
            if a%i==0:
                factors_a.append(i)
        for i in range(1,b+1):
            if b%i==0:
                factors_b.append(i)
        common=[]
        for i in factors_a:
            for j in factors_b:
                if i==j:
                    common.append(i)
        return common[-1]
