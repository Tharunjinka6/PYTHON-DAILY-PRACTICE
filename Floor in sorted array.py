class Solution:
    def findFloor(self, arr, x):
        # code here
        for i in range(len(arr)-1,-1,-1):
            if x<arr[0]:
                return -1
            elif arr[i]==x:
                return i
            elif arr[i]<x:
                return i
        return len(arr)-1