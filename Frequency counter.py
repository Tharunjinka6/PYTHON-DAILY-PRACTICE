#used chatgpt and learned this
class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        list1 = [0] * n
        for num in arr:
            if 1 <= num <= n:
                list1[num - 1] += 1
        return list1

#Time complexity 0(n^2) so it is not working in geeks for greeks
arr=[2,3,2,3,5]
n=len(arr)
list=[]
for i in range(1,n+1):
    count=0
    for num in arr:
        if num==i:
            count+=1
    list.append(count)
print(list)