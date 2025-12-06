class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = None
        self.recursive(root,k)
        return self.ans
    def recursive(self,node,k):
        if node is None:
            return 
        self.recursive(node.left,k)
        self.count+=1
        if self.count == k:
            self.ans = node.val
            return 
        self.recursive(node.right,k)

        