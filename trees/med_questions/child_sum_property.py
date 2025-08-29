class Solution:
    def checkChildrenSum(self, root: TreeNode) -> int:
        # Base Case: If tree is empty or a leaf node
        if root is None or (root.left is None and root.right is None):
            return 1  # A leaf or empty tree trivially satisfies CSP

        # Get values of children (0 if child doesn't exist)
        left_val = root.left.val if root.left else 0
        right_val = root.right.val if root.right else 0

        # Check current node and recursively check left & right subtrees
        if root.val == left_val + right_val and \
           self.checkChildrenSum(root.left) and \
           self.checkChildrenSum(root.right):
            return 1  # Satisfies property
        else:
            return 0  # Does not satisfy

