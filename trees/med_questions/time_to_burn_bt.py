from collections import deque
class Solution:
    def markparents(self, root ,map1):
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr.left:
                map1[curr.left] = curr # son ->parent
                q.append(curr.left)
            if curr.right:
                map1[curr.right] = curr # son ->parent
                q.append(curr.right)
    def timeToBurnTree(self, root, start):
        # this assumes if start is a treenode
        # is start is a int u just make start = treenode using dfs or bfs
        q = deque()
        map1 = {}
        self.markparents(root,map1)
        visited = {}
        q.append(start)
        visited[start] = True
        time = 0
        while q:
            size = len(q)
            new_fire = False # Flag to check if fire spreads this round 
            for i in range(size):
                curr = q.popleft()
                if curr.left and curr.left not in visited:
                    q.append(curr.left)
                    visited[curr.left] = True
                    new_fire = True
                if curr.right and curr.right not in visited:
                    q.append(curr.right)
                    visited[curr.right] = True
                    new_fire = True
                if curr in map1 and map1[curr] not in visited:
                    q.append(map1[curr])
                    visited[map1[curr]] = True
                    new_fire = True
            time += 1
        return time

