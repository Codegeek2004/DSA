import collections
class Solution(object):
    def singleNumber(self, nums):
        k=collections.Counter(nums)
        for i in k:
            if(k[i]!=3):
                l=i
        return l
       
        