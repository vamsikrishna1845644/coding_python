class Solution:
    # i thinbk i cannot come up with this code so check
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.recursive(root.left , root.right)
    def recursive(self,left,right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.recursive(left.left,right.right) and self.recursive(left.right,right.left)