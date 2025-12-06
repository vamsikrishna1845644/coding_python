from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m= len(grid[0])
        # create visited matrix
        vis = [[0]*m for _ in range(n)]
        # for all rotten oranges call bfs
        time = 0

        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j,0])
                if grid[i][j] == 1:
                    # mark them
                    vis[i][j] = 1
        while q:
            i ,j ,clock = q.popleft()
            time = max(time,clock) # update the max time

            # check in 4 directions
            for delr in [-1,0,1]:
                for delc in [-1,0,1]:
                    # only to move in 4 directions
                    if (delr == 0 and (delc == 1 or delc == -1)) or (delc == 0 and (delr == 1 or delr == -1)):
                        newr = i + delr
                        newc = j + delc
                        if newr >=0 and newr < n and newc >=0 and newc<m and vis[newr][newc] == 1:
                            # mark it as rotten
                            vis[newr][newc] = 2
                            # append it to the queue as it is a rotten
                            q.append([newr,newc,clock+1])
        
        # check if there are any fresh oranges
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 1:
                    return -1
        return time

        
