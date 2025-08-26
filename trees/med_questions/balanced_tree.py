class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
         ans = self.recursive(root)
         if ans == -1:
              return False
         return True
    def recursive(self, root):
         if root is None:
              return 0
         
         left = self.recursive(root.left)
         if left == -1:
              return -1
         right = self.recursive(root.right)
         if right == -1:
              return -1
         if abs( left - right) > 1:
              return -1
         return 1 + max(left , right)

         