# Time complexity is O(n)
# Space complexity for n time calling recursion O(n)
class Solution:
	def is_sorted_array(self,nums,idx) -> bool:
		if idx == len(nums)-1:
			return True
		if nums[idx] <= nums[idx+1]:
			return self.is_sorted_array(nums,idx+1)
		return False

if __name__ == "__main__":
	solution = Solution()
	print(solution.is_sorted_array([1,2,8,4,2,7,5,2],0))
	print(solution.is_sorted_array([1,2,3,4,5,6],0))