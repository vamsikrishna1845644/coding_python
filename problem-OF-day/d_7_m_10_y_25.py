from typing import List
from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # solving this using grphs
        # declared the visited array
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for _ in range(n)]

        # should use bfs algo
        q = deque()
        q.append([0,0]) # [row,col]
        vis[0][0] = 1
        min_t = 0
        max_t = 0
        while q:
            row , col = q.popleft()

            delr = [-1, 1, 0, 0]
            delc = [0, 0, -1, 1]
            neighbour = []
            ind = []
            # 4 direction movement
            for r in delr:
                for c in delc:
                    newr = row + r
                    newc = col + c

                    if (newr >=0 and newr < n) and (newc >=0 and newc < m) and not vis[newr][newc]:
                        neighbour.append(grid[newr][newc])
                        ind.append([newr,newc])

            if neighbour:  # means list is not empty
                min_t = min(neighbour)
                ele = neighbour.index(min_t)
                q.append(ind[ele])
                ne, co = ind[ele]
                vis[ne][co] = 1
            else:
                continue

        if vis[n-1][m-1] == 1:
            return max_t
        else:
            return 0





