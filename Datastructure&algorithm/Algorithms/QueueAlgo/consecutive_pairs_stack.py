from Queue import LinkedQueue
class Solution:
    def __repr__(self) -> str:
        nums = [4,5,-2,-3,11,10,5,6,0,1]
        return str(self.checkPairConsecutive(nums))
    def checkStackPairwiseOrder(self,nums: list)->bool:
        pairwiseOrder = True
        queue = LinkedQueue()
        while len(nums) != 0:
            queue.enQueue(nums.pop())
        while queue.isEmpty() is False:
            nums.append(queue.deQueue())
        while len(nums) != 0:
            n = nums.pop()
            queue.enQueue(n)
            if len(nums) != 0:
                m = nums.pop()
                queue.enQueue(m)
                if abs(m-n) != 1:
                    pairwiseOrder = False
        while queue.isEmpty() is False:
            nums.append(queue.deQueue())
        return pairwiseOrder
    def checkPairConsecutive(self,nums)->bool:
        i = 0
        while i < len(nums):
            if i + 1 < len(nums):
                if abs(nums[i]-nums[i+1]) != 1:
                    return False
            else:
                return False
            i+=2
        return True
if __name__ == "__main__":
    print(Solution())