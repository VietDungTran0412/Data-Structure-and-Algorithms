from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def getBST(self)->BinarySearchTreeNode:
        preorder = [1,2,4,5,8,3,6,7,9,10]
        inorder = [4,2,8,5,1,6,3,9,7,10]
        self.preOrderIndex = 0
        root = self.buildBSTfromSequence(inorder,preorder,0,len(inorder)-1)
        return root
    def search(self,nums,start,end,val)->int:
        for i in range(start,end+1):
            if nums[i] == val:
                return i
    def buildBSTfromSequence(self,inorder: list, preorder: list, inOrderStart: int, inOrderEnd:int)->BinarySearchTreeNode:
        if inOrderStart > inOrderEnd:
            return None
        newVal = preorder[self.preOrderIndex]   
        newNode = BinarySearchTreeNode(newVal)
        self.preOrderIndex += 1
        if inOrderEnd == inOrderStart:
            return newNode
        inOrderIndex = self.search(inorder,inOrderStart,inOrderEnd,newNode.data)
        newNode.left = self.buildBSTfromSequence(inorder,preorder,inOrderStart,inOrderIndex-1)
        newNode.right = self.buildBSTfromSequence(inorder,preorder,inOrderIndex+1,inOrderEnd)
        return newNode
root = Solution().getBST()
print(root.preorder())