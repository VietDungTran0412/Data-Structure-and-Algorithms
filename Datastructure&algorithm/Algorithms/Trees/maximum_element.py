from Tree import BinarySearchTreeNode,build_tree

class Solution:
    def __repr__(self) -> str:
        elements = [2,4,1,6,7,22,12,9,21,20,55]
        root = build_tree(elements)
        return str(self.findMaxNonRecursive(root))
    def findMaxBST(self,root)->int: # Depth First Search Approach
        max = -1000000
        if root != None:
            root_val = root.data
            left = self.findMaxBST(root.left)
            right = self.findMaxBST(root.right)
            if left < right:
                max = right
            else:
                max = left
            if root_val > max:
                max = root_val
        return max
    def findMaxNonRecursive(self,root)->int: # Breadth First Search Approach
        if root is None:
            return -1
        queue = [root]
        i = 0
        max = -1000000
        while i < len(queue):
            if queue[i].data > max:
                max = queue[i].data
            if queue[i].left:
                queue.append(queue[i].left)
            if queue[i].right:
                queue.append(queue[i].right)
            i+=1
        return max

print(Solution())