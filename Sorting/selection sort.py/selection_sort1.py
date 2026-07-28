arr=[2,5,1,0,-1]
size=len(arr)
for i in range(size-1):
    min_index=i
    for j in range(i+1,size):
        if arr[j]<arr[min_index]:
            min_index=j
    if i!=min_index:
        arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)
