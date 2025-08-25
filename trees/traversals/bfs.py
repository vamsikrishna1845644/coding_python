from collections import deque

def bfs(node):
    ans = []
    if node is None:
        return ans
    
    q = deque()
    q.append(node)
    
    while q:  # Loop while queue is NOT empty
        size = len(q)
        level = []
        
        for _ in range(size):
            element = q.popleft()
            
            # Add children to queue
            if element.left != None:
                q.append(element.left)
            if element.right is not None:
                q.append(element.right)
            
            level.append(element.val)
        
        ans.append(level)
    
    return ans
