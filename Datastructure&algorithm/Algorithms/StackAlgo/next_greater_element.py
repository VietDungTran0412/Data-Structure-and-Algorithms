from stack import DynamicStack
class Solution:
    def printSolution(self):
        nums1 = [2,4]
        nums2 = [1,2,3,4]
        print(self.nextGreaterElement(nums1,nums2))
    def nextGreaterElement(self,nums1: list, nums2: list)->list:
        stack = DynamicStack()
        greaterNums = {}
        stack.push(len(nums2)-1)
        for i in range(len(nums2)-1,-1,-1):
            while stack.isEmpty() is False and nums2[stack.peek()] <= nums2[i]:
                stack.pop()
            if stack.isEmpty():
                greaterNums[nums2[i]] = -1
            else:
                greaterNums[nums2[i]] = nums2[stack.peek()]
            stack.push(i)
        res = []
        for num in nums1:
            res.append(greaterNums[num])
        return res
        
Solution().printSolution()