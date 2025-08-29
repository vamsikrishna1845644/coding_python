from collections import deque
class Solution:
    def markparents(self,root,target,map1):
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr.left:
                map1[curr.left] = curr
                q.append(curr.left)
            if curr.right:
                map1[curr.right] = curr
                q.append(curr.right)
            
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        map1 = {}
        self.markparents(root,target,map1)
        visited = {}
        q = deque()
        q.append(target)
        visited[target]  = True
        curr_level = 0
        while q:
            size = len(q)
            if curr_level == k:
                break
            for i in range(size):
                curr = q.popleft()
                 # Left
                if curr.left and curr.left not in visited:
                    q.append(curr.left)
                    visited[curr.left] = True

                # Right
                if curr.right and curr.right not in visited:
                    q.append(curr.right)
                    visited[curr.right] = True

                # Parent
                if curr in map1 and map1[curr] not in visited:
                    q.append(map1[curr])
                    visited[map1[curr]] = True
            curr_level+=1
        ans = [] # to store ans
        for i in q:
            ans.append(i.val)
        return ans