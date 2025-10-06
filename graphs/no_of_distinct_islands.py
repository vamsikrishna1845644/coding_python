class Solution:
    def count_distinct_islands(self,grid):
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for _ in range(n)]
        # using dfs alogo ,
        # first check for ones in the grid
        self.ans = set() # set  of tuples as elemnets should be immutable
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]: # only if its not visited
                    path = [] # to store the path for the island
                    self.dfs(i,j,vis,grid,path,i,j)
                    self.ans.add(tuple(path)) # add to our main answer
        return len(self.ans)
    def dfs(self,row,col,vis,grid,path,baser,basec):
        # mark as visited
            vis[row][col] = 1
            n = len(grid)
            m = len(grid[0])
            # add relative path
            path.append((row-baser,col-basec))

        # move in 4 directions
            delr = [-1,0,1,0]
            delc = [0,1,0,-1]
            for i in range(4):
                newr = row + delr[i]
                newc = col + delc[i]
                # check for valid newr,newc
                if newr >=0 and newr <n and newc >=0 and newc < m and not vis[newr][newc] and grid[newr][newc] == 1:
                    # go to the depths of it 
                    self.dfs(newr,newc,vis,grid,path,baser,basec)

if __name__ == "__main__":
 grid = [
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 1]
 ]
sol = Solution()
print(sol.count_distinct_islands(grid))


 
