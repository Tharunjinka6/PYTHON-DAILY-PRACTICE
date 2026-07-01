arr=[2,3,2,3,5]
sorted_arr=sorted(arr)
n=arr[-1]
count_2=0
count_3=0
count_5=0
for i in range(1,n+1):
    if i==2:
        count_2+=1
    elif i==3:
        count_3+=1
    elif i==5:
        count_5+=1
print(count_2,count_3,count_5)