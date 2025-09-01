class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        curr = root.val
        if curr<p.val and curr<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if curr>p.val and curr>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return root