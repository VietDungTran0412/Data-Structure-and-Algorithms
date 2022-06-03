# Time complexity O(2^n)
class Solution:
	def tower_of_hanoi(self,n,frompeg,topeg,auxpeg) -> None:
		if n ==1:
			print(f"Move {n} from peg {frompeg} to {topeg}")
			return
		self.tower_of_hanoi(n-1,frompeg,auxpeg,topeg)
		print(f"Move {n} from peg {frompeg} to {topeg}")
		self.tower_of_hanoi(n-1,auxpeg,topeg,frompeg)
	
if __name__ == "__main__":
	solution = Solution()
	print(solution.tower_of_hanoi(5,"A","B","C"))