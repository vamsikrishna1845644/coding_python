class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        arr = [float('-inf')] # int min
        self.recursive(root , arr)
        return int(arr[0])
    def recursive(self,node , maxi):
        if node is None:
            return 0
        left = max(0,self.recursive(node.left,maxi))
        right = max(0,self.recursive(node.right,maxi))
        maxi[0] = max(maxi[0] , left + right + node.val)
        return node.val + max(left,right)
