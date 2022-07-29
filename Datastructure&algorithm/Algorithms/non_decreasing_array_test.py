import unittest
from non_decreasing_array import Solution
class Test(unittest.TestCase):
    def test_result(self):
        nums = [5,3,4,4,7,3,6,11,8,5,11]
        res = Solution().totalStepNonDecreasingArray(nums)
        self.assertEqual(res,3)
        print("Expected: 3")
        print("Your result: "+ str(res))
    def test_result2(self):
        nums = [4,5,7,7,13]
        res = Solution().totalStepNonDecreasingArray(nums)
        self.assertEqual(res,0)
if __name__ == "__main__":
    unittest.main()