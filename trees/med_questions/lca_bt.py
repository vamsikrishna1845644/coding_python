class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
         return self.recursive(root , p ,q)
    def recursive(self, root ,p ,q):
          if root == None or root ==  p or root == q:
              return root
          left = self.recursive(root.left,p,q)
          right = self.recursive(root.right,p,q)
          if left is None:
               return right
          elif right is None:
               return left
          else:
               return root