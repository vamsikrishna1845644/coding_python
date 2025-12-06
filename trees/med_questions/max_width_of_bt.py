# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        width = 0
        q.append([root , 0]) # [root,  y_level]
        ans = 0
        while q:
            size = len(q)
            min1 = q[0][1]
            first,last = 0,0
            for i in range(size):
                curr = q[0][1] - min1
                node ,idx = q.popleft()
                if i == 0:
                    first = curr
                if i == size - 1:
                    last = curr
                if node.left is not None:
                    q.append([node.left,2*curr + 1])
                if node.right is not None:
                    q.append([node.right,2*curr+2])
            ans= max(ans , last - first +1)
        return ans