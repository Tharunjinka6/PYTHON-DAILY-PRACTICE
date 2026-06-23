class Solution:
    def getMinMax(self, arr):
        # code here
        arr.sort()
        return([arr[0],arr[-1]])
    
#without using builtinfunction
class Solution:
    def getMinMax(self, arr):
        # code here
        min=arr[0]
        max=arr[0]
        for i in arr:
            if i<min:
                min=i
            if i>max:
                max=i
        return [min,max]
        