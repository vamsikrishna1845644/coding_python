from collections import deque,defaultdict
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root):
        q = deque()
        ans = defaultdict(lambda: defaultdict(list)) # key -> int(x axis) , value is map of y axis and list 
        q.append([root,0,0]) # [node,x axis , y axis]
        res = []
        while q:
            nodelist = q.popleft()
            ans[nodelist[1]][nodelist[2]].append(nodelist[0].val)
            if nodelist[0].left is not None:
                q.append([nodelist[0].left,nodelist[1]-1,nodelist[2]+1])
            if nodelist[0].right is not None:
                q.append([nodelist[0].right,nodelist[1]+1,nodelist[2]+1])
            
        for x in sorted(ans.keys()):
            col = []
            for y in sorted(ans[x].keys()):
                col.extend(sorted(ans[x][y]))
            res.append(col)
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
print(sol.verticalTraversal(root))