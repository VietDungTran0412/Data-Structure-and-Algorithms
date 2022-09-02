from Tree import BinarySearchTreeNode,build_tree

class Solution:
    def print_solution(self):
        root = build_tree([5,2,7,19,15,9,12]) 
        head = self.convert(root)[0]
        cur = head
        while cur:
            print(cur.data)
            cur = cur.right

    def convert(self,root:BinarySearchTreeNode):
        if root is None:
            return [None,None]
        if root.left is None and root.right is None:
            return [root,root]
        left = self.convert(root.left)
        right = self.convert(root.right)

        res = [None,None]

        if left[0] != None and left[1] != None:
            left[1].right = root
            root.left = left[1]
            res[0] = left[0]
        else:
            res[0] = root
        

        if right[0] != None and right[1] != None:
            right[0].left = root
            root.right = right[0]

            res[1] = right[1]
        else:
            res[1] = root
        return res






    
Solution().print_solution()


#           5
#       10      15
#         25 30  35 
#--> 20-10-25-5-30-15-35
#
#