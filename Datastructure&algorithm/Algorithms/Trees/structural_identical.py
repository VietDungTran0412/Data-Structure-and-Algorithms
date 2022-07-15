from Tree import BinarySearchTreeNode, build_tree
class Solution:
    def __repr__(self) -> str:
        nums1 = [8,3,9,5,10,14,12,4,16,13]
        nums2 = [8,3,9,5,10,14,12,4,16,13]
        root1 = build_tree(nums1)
        root2 = build_tree(nums2)
        return str(self.areStructuralIdentical(root1,root2))
    def areStructuralIdentical(self,root1:BinarySearchTreeNode, root2: BinarySearchTreeNode)->bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.data == root2.data and self.areStructuralIdentical(root1.left,root2.left)
                and self.areStructuralIdentical(root1.right,root2.right))
print(Solution())