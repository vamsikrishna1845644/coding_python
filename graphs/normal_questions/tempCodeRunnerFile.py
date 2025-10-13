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
                if grid[i][j] == 1:
                    vis[i][j] = 1
                    self.dfs(i,j,vis,grid)
        return len(ans)
    def dfs(self,row,col,vis,grid):
        # mark as visited
            vis[row][col] = 1
            n = len(grid)
            m = len(grid[0])
            tup = []

        # move in 4 directions
            delr = [-1,0,1,0]
            delc = [0,1,0,-1]
            for i in range(4):
                newr = row + delr[i]
                newc = col + delc[i]
                if i == 0: # base
                    baser = newr
                    basec = newc
                # check for valid newr,newc
                if newr >=0 and newr <n and newc >=0 and newc < m and not vis[newr][newc] and grid[newr][newc] == 1:
                    # mark as visited
                    vis[newr][newc] = 1
                    # add to tuple
                    tup.append([newr - baser,newc - basec])
                    # add to set
                    # go to the depths of it 
                    self.dfs(newr,newc,vis,grid)
            #  convert to a tuple of tuple to place it in a set       
            tup = tuple(map(tuple,tup))
            # add to global set
            self.ans.add(tup)