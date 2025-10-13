from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # doing this question on my own
        n = len(mat)
        m = len(mat[0])
        dist = [[-1]*m for _ in range(n)]
        # using bfs
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append([i,j])
        while q:
            r,c = q.popleft()
            for delr in [-1,0,1]:
                for delc in [-1,0,1]:
                    # we need only 4 directions
                    if (delr == 0 and ( delc == 1 or delc == -1)) or (delc == 0 and (delr == 1 or delr == -1)):
                        newr = r + delr
                        newc = c + delc
                        if newr>=0 and newr< n and newc >=0 and newc<m and dist[newr][newc] == -1: # unvisted
                            dist[newr][newc]  = dist[r][c] + 1
                            q.append([newr,newc])
        return dist                    
