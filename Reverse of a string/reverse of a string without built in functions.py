class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        list1=[]
        for i in s[::-1]:
            list1.append(i)
        s1=''.join(list1)
        return s1
        