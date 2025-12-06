from typing import List,Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        map1 = {}
        for i in range(len(inorder)):
            map1[inorder[i]] = i # value -> index

        root = self.build(postorder , 0 ,len(postorder) - 1 ,inorder , 0,len(inorder) - 1,map1)
        return root
    def build(self,postorder,poststart,postend,inorder,instart,inend,map1):
        if poststart > postend or instart > inend :
            return None
        root = TreeNode(postorder[postend])
        inroot = map1[postorder[postend]]
        numsleft = inroot - instart
        root.left = self.build(postorder , poststart,poststart+numsleft-1,inorder,instart,inroot-1,map1)
        root.right = self.build(postorder , poststart+numsleft,postend - 1,inorder,inroot+1,inend,map1) 
        return root
    