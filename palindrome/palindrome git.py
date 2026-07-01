class Solution:
    def isPalindrome(self, s):
        # code here
        s_lower=s.lower()
        new_s=""
        for i in s_lower[::-1]:
            new_s=new_s+i
        if s_lower==new_s:
            return True
            

