#using Built-in Functions
class Solution:
    def areAnagrams(self, s1, s2):
       list_s1=list(s1)
       list_s2=list(s2)
       sorted_s1=sorted(list_s1)
       sorted_s2=sorted(list_s2)
       if sorted_s1==sorted_s2:
           return True
       else:
           return False
       
#time limit exceeded in Geeks for Greeks
class Solution:
    def areAnagrams(self, s1, s2):
       list_s1=list(s1)
       list_s2=list(s2)
       for i in range(len(list_s1)-1):
           for j in range(len(list_s1)-i-1):
               if ord(list_s1[j])>ord(list_s1[j+1]):
                   Temp=list_s1[j]
                   list_s1[j]=list_s1[j+1]
                   list_s1[j+1]=Temp
       result1="".join(list_s1)
       for i in range(len(list_s2)-1):
           for j in range(len(list_s2)-i-1):
               if ord(list_s2[j])>ord(list_s2[j+1]):
                   Temp=list_s2[j]
                   list_s2[j]=list_s2[j+1]
                   list_s2[j+1]=Temp
       result2="".join(list_s2)
       if result1==result2:
           return True
       else:
           return False


#works only when the two strings have the same charcters
str1="tharun"
Ascii_1=0
str2="tahurn"
Ascii_2=0
for i in str1:
    Ascii_1=Ascii_1+ord(i)
for j in str2:
    Ascii_2=Ascii_2+ord(j)
if Ascii_1==Ascii_2:
    print("Anagram")
else:
    print("not a Anagram")
