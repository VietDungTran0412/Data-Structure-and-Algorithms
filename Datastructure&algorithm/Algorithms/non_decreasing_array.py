class Node:
    def __init__(self,val = 0) -> None:
        self.val = val
        self.next = None
class Solution:
    def totalStepNonDecreasingArray(self,nums: list):
        minLeft = nums[0]
        count  = 0
        res = 0
        for i in range(1,len(nums)):
            if nums[i] >= minLeft:
                minLeft = nums[i]
                res = max(count,res)
                count  = 0
            else:
                count += 1
        return res