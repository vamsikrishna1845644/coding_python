from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        stack = deque([root])
        ans = []
        flag = False # false means left -> right
        while stack:
            size = len(stack)
            level = []
            for i in range(size):
                node = stack.popleft()
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
                level.append(node.val)
            if flag == False:
                ans.append(level)
                flag = True
            else:
                ans.append(level[::-1])
                flag = False
                