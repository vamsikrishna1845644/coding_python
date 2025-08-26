from collections import deque,defaultdict
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def topView(self, root):
        q = deque() 
        ans = defaultdict(int)
        res = [] # to return ans
        q.append([root,0])
        while q:
            node,x =q.popleft()
            if x not in ans:
                ans[x]= node.val
            if node.left is not None:
                q.append([node.left,x-1])
            if node.right is not None:
                q.append([node.right,x+1])
        for x in sorted(ans.keys()):
            res.append(ans[x])
        return res
    
if __name__ == "__main__":
# Create the root node
    root = Node(1)

# Create the left subtree
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)

# Create the right subtree
    root.right = Node(3)
    root.right.right = Node(6) # Note: The left child of 3 is None

# --- Test your function ---
sol = Solution()
print(sol.topView(root))