def Binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[5,12,18,23,35,47,59,63,72,88]
key=47
result=Binary_search(arr,key)
if result!=-1:
    print("The key value is found at",result)
else:
    print("The key value not found")