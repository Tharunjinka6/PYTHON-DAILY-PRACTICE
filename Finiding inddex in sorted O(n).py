#my practiced code
arr=[1,2,3,4,6,7]
key=5
for i in range(len(arr)):
    if arr[i]==key:
        print(i)
    elif arr[i]>key:
        print(i)
        break

#GeekforGeeks
class Solution:
    def searchInsertK(self, arr, k):
        # code here
        for i in range(len(arr)):
            if arr[i]==k:
                return i
            elif arr[i]>k:
                return i
        return len(arr)

        