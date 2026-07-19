arr=[1,3,2,5,7,8]
for i in range(len(arr)):
    for j in range(i):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)