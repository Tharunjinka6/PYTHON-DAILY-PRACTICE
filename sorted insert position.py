#practiced code using trail and error
def sip(arr,k):
    new_arr=arr[:]
    if k in arr:
        print("The element is present at",arr[k])
    else:
        new_arr.append(k)
        new_arr.sort()
        print("The elment should be placed at index",new_arr.index(k))
arr=[1,2,3,4,6]
k=5
sip(arr,k)
#geeks for geeks
class Solution:
    def searchInsertK(self, arr, k):
        # code here
        new_arr=arr[:]
        if k in arr:
            return arr.index(k)
        else:
            new_arr.append(k)
            new_arr.sort()
            return new_arr.index(k)
