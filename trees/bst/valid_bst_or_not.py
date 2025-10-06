class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root,float('-inf'),float('inf'))
    def valid(self,node,min,max):
        if node is None:
            return True
        if node.val>=max or node.val<=min:
            return False
        return self.valid(node.left,min,node.val) and self.valid(node.right,node.val,max)
    