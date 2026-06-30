#without using Built-in functions
str=input("Enter the string:").lower()
vowels=["a","e","i","o","u"]
count=0
for i in str:
    for j in vowels:
        if i == j:
            count=count+1
print(count)

#using built-in function
str1=input("Enter the string:").lower()
vowels1=["a","e","i","o","u"]
count1=0
for i in str1:
    if i in vowels1:
        count1=count1+1
print(count1)