class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
       return self.recursive(root,val)
    def recursive(self,node,val):
        # base case
        if node is None:
            return None
        
        if node.val == val:
            return node
        if val<node.val:
           return self.recursive( node.left ,val)
        if val>node.val:
            return self.recursive( node.right ,val)
        