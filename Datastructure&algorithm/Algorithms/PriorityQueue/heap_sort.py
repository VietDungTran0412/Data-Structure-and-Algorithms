import heapq
import unittest
class Solution:
    def heapSort(self,nums):
        newAr = []
        heapq.heapify(nums)
        for i in range(len(nums)):
            newAr.append(heapq.heappop(nums))
        for j in range(len(newAr)):
            nums.append(newAr[j])
class TestSort(unittest.TestCase):
    ar =[2,1,5,4,3,8,7,6]
    def testAr(self):     
        Solution().heapSort(self.ar)
        self.assertEqual([1,2,3,4,5,6,7,8],self.ar)
unittest.main()