class Solution:
    def rotate(self, arr):
        k=1
        n=len(arr)
        rotated_arr=[0]*n
        for i in range(n):
            rotated_arr[(i+k)%n]=arr[i]
        arr[:] = rotated_arr