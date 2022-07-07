from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def reverseLevelOrderTraversal(self,root:BinarySearchTreeNode):
        if root is None:
            print("Empty Tree!")
            return
        elements = [root]
        i = 0
        while i < len(elements):
            if elements[i].right:
                elements.append(elements[i].right)
            if elements[i].left:
                elements.append(elements[i].left)
            i+=1
        while len(elements) != 0:
            temp = elements.pop()
            print(temp.data,end=" ")
root = build_tree([5,2,6,8,10,12,9,11,20,15])
Solution().reverseLevelOrderTraversal(root)