str1=input("Enter the string:").lower()
set_str=set(str1)
vowels=["a","e","i","o","u"]
vowels_set=set(set_str)
count=0
for i in set_str:
    for j in vowels:
        if i == j:
            count=count+1
print(count)

#using built-in function
str2=input("Enter the string:").lower()
set_str2=set(str2)
vowels1=["a","e","i","o","u"]
vowels_set=set(set_str2)
count1=0
for i in set_str2:
    if i in vowels1:
        count1=count1+1
print(count1)