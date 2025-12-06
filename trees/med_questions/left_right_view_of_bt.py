class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans =  [] # to store the ans
        self.recursive(root , 0 ,ans)
        return ans
    def recursive(self , node , level ,ans):
        if node is None:
            return 
        if level == len(ans):
            ans.append(node.val)
        self.recursive(node.right,level + 1, ans) # for go right then left
        self.recursive(node.left , level + 1 , ans)

