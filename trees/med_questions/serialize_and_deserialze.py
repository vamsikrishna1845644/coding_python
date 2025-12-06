from collections import deque
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        
        res = ""
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                res += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)
            else:
                res += "#,"
        
        return res
               

    def deserialize(self, data):
        if not data:
            return None
        
        nodes = data.split(",")[:-1]  # Remove last empty element
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        
        while q and i < len(nodes):
            node = q.popleft()
            
            # Left child
            if nodes[i] != "#":
                left = TreeNode(int(nodes[i]))
                node.left = left
                q.append(left)
            i += 1
            
            # Right child
            if i < len(nodes) and nodes[i] != "#":
                right = TreeNode(int(nodes[i]))
                node.right = right
                q.append(right)
            i += 1
        
        return root

