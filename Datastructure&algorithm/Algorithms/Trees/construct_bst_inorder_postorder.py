from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def getBST(self)->BinarySearchTreeNode:
        postorder = [3,2,6,5,14,1,20,15,7]
        inorder = [2,3,5,6,7,1,14,15,20]
        self.postOrderIdx = len(inorder)-1
        root = self.buildBSTfromSequence(inorder,postorder,0,len(inorder)-1)
        return root
    def search(self,nums,start,end,val)->int:
        for i in range(start,end+1):
            if nums[i] == val:
                return i
    
    def buildBSTfromSequence(self,inorder: list, postorder: list, inOrderStart: int, inOrderEnd:int)->BinarySearchTreeNode:
        if inOrderStart>inOrderEnd:
            return None
        val = postorder[self.postOrderIdx]
        newNode = BinarySearchTreeNode(val)
        self.postOrderIdx -= 1
        if inOrderStart == inOrderEnd:
            return newNode
        postOrderIdx = self.search(inorder,inOrderStart,inOrderEnd,val)
        newNode.right = self.buildBSTfromSequence(inorder,postorder,postOrderIdx+1,inOrderEnd)
        newNode.left = self.buildBSTfromSequence(inorder,postorder,inOrderStart,postOrderIdx-1)
        return newNode
        
root = Solution().getBST()
print(root.postorder())
