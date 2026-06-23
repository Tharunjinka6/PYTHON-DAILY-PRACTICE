class Solution:
    def search(self, arr, x):
        # code here
        if x in arr:
            return(arr.index(x))
        else:
            return -1

# without built-in functions
class Solution:
    def search(self, arr, x):
        # code here
        for i in arr:
            if i == x:
                return (arr.index(x))
        return -1
        
