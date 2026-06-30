arr=[2,3,2,3,5]
n=len(arr)
new_list=[]
for i in range(n):
    for j in range(i):
        arr[j]==arr[j+1]
        new_list.append(arr[j])
print(new_list)

