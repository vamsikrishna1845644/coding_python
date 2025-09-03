from collections import deque
from typing import List

class Solution1:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)]
        
        # Step 1: Mark all boundary-connected land cells
        # Check all boundary cells
        for i in range(n):
            for j in range(m):
                # If it's a boundary cell and is land and not visited
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and grid[i][j] == 1 and not vis[i][j]:
                    self.bfs(i, j, vis, grid)
        
        # Step 2: Count remaining unvisited land cells (these are enclaves)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    count += 1
        
        return count
    
    def bfs(self, row, col, vis, grid):
        n = len(grid)
        m = len(grid[0])
        
        q = deque([(row, col)])
        vis[row][col] = True
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                newr = r + dr
                newc = c + dc
                
                # Check bounds and conditions
                if (0 <= newr < n and 0 <= newc < m and 
                    not vis[newr][newc] and grid[newr][newc] == 1):
                    vis[newr][newc] = True
                    q.append((newr, newc))
#############################
#best Solution

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for _ in range(n)]
        # doing using bfs
        q = deque() # put all boundary land nodes in que and do bfs on each of them

        # use boundary conditions adn multi node bfs
        for j in range(m):
            if  grid[0][j] == 1:
                q.append([0,j])
                vis[0][j] = 1
            if   grid[n-1][j] == 1:
                q.append([n-1,j])
                vis[n-1][j] = 1
        for i in range(n):
            if  grid[i][0] == 1:
                q.append([i,0])
                vis[i][0] = 1
            if  grid[i][m-1]== 1:
                q.append([i,m-1])
                vis[i][m-1] = 1
        
        while q:
            row,col = q.popleft()
            # check in 4 directions
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for delr,delc in directions:
                newr = row + delr
                newc = col + delc
                if newr>=0 and newr<n and newc >=0 and newc <m and not vis[newr][newc] and grid[newr][newc] == 1:
                    # mark as visted
                    vis[newr][newc] = 1
                    q.append([newr,newc])

        # count middle remaing untouched land
        count = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    count+=1      
        return count
   
