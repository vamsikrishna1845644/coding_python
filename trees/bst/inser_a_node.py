class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head = root
        if root is None:
            new = TreeNode(val)
            return new
        while root:
            if val<root.val :
                if root.left is not None:
                    root = root.left 
                else:
                    node = TreeNode(val)
                    root.left = node
                    break
            if root.val<=val:
                if root.right is not None:
                    root = root.right 
                else:
                    node = TreeNode(val)
                    root.right = node
                    break
        return head

