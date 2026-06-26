
class Solution:
    def getSecondLargest(self, arr):
        largest = float('-inf')
        second = float('-inf')

        for num in arr:
            if num > largest:
                second = largest
                largest = num
            elif num > second and num != largest:
                second = num

        if second == float('-inf'):
            return -1

        return second

    #using bubble sort my method
    # def bubblesort(arr):
    # n=len(arr)
    # for i in range(n-1):
    #     for j in range(n-i-1):
    #         if arr[j]>arr[j+1]:
    #             temp=arr[j]
    #             arr[j]=arr[j+1]
    #             arr[j+1]=temp
    # return arr
      
    # arr=[10,5,11,9,60]
    # sorted_arr=bubblesort(arr)
    # print(sorted_arr)
    # print(sorted_arr[-2])
