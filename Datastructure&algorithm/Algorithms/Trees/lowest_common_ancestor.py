from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2,7,10,6,4,3,1])
        res = self.findLowestCommonAncestorRecur(root,BinarySearchTreeNode(3),BinarySearchTreeNode(2))
        return str(res.data)
    def findLowestCommonAncestor(self,root: BinarySearchTreeNode,p: BinarySearchTreeNode, q: BinarySearchTreeNode)->BinarySearchTreeNode:
        cur = root
        while cur:
            if cur.data > p.data and cur.data > q.data:
                cur = cur.left
            elif cur.data < p.data and cur.data < q.data:
                cur = cur.right
            else:
                return cur
    def findLowestCommonAncestorRecur(self,root:BinarySearchTreeNode,p:BinarySearchTreeNode,q:BinarySearchTreeNode)->BinarySearchTreeNode:
        if root is None:
            return None
        if root.data > p.data and root.data > q.data:
            return self.findLowestCommonAncestorRecur(root.left,p,q)
        if root.data < p.data and root.data < q.data:
            return self.findLowestCommonAncestorRecur(root.right,p,q)
        return root
print(Solution())    