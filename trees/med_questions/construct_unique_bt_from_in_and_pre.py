from typing import List,Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map1 = {}
        for i in range(len(inorder)):
            map1[inorder[i]] = i # value -> index

        root = self.build(preorder , 0 ,len(preorder) - 1 ,inorder , 0,len(inorder) - 1,map1)
        return root
    def build(self,preorder,prestart,prend,inorder,instart,inend,map1):
        if prestart > prend or instart > inend :
            return None
        root = TreeNode(preorder[prestart])
        inroot = map1[root.val]
        numsleft = inroot - instart
        root.left = self.build(preorder , prestart+1,prestart+numsleft,inorder,instart,inroot-1,map1)
        root.right = self.build(preorder , prestart+numsleft+1,prend,inorder,inroot+1,inend,map1) 
        return root
    