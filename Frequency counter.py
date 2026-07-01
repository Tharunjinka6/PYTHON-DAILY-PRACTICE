arr=[2,3,2,3,5]
sorted_arr=sorted(arr)
n=len(arr)
new_list=[]
for i in range(n-1):
    for j in range(n-1):
        arr[j]==arr[j+1]
        new_list.append(arr[j])
print(new_list)

