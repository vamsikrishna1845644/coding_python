class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.lheight(root)
        right = self.rheight(root)
        if left == right:
            return 2**(left) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    def lheight(self,node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h
    def rheight(self,node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h
    