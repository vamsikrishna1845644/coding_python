class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max1 = 0
        self.recursive(root)
        return self.max1
    def recursive(self, root):
        if root == None:
            return 0
        
        left = self.recursive(root.left)
        right = self.recursive(root.right)
        self.max1  = max(self.max1 , left + right)
        return 1 + max (left, right)
