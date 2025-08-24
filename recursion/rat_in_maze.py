class Solution:
    def findPath(self, grid):
        ans = [] # to store ans
        move = ""
        n = len(grid)
        vis=[[0]*n for _ in range(n)] # vsiited grid of n*n 
        if grid[0][0] == 1:
            vis[0][0] = 1 # mark the first cell vsisited
            self.recursive(0,0,grid,ans,move,n,vis)
            return ans
    def recursive(self,i ,j ,grid, ans, move ,n,vis):
        # base case
        if i == n-1 and j == n-1:
            ans.append(move[:])
            return
        
        #down
        if i+1<n and not vis[i+1][j] and grid[i+1][j] == 1:
            vis[i+1][j] = 1
            self.recursive(i+1 ,j ,grid, ans, move +"D" ,n,vis)
            vis[i+1][j] = 0 # backtrack

        #left
        if j-1>=0 and not vis[i][j-1] and grid[i][j-1] == 1:
            vis[i][j-1] = 1
            self.recursive(i ,j-1,grid, ans, move +"L" ,n,vis)
            vis[i][j-1] = 0 # backtrack
            
        #right
        if j+1<n and not vis[i][j+1] and grid[i][j+1] == 1:
            vis[i][j+1] = 1
            self.recursive(i ,j+1 ,grid, ans, move +"R" ,n,vis)
            vis[i][j+1] = 0 # backtrack
            
        #up
        if i-1>=0 and not vis[i-1][j] and grid[i-1][j] == 1:
            vis[i-1][j] = 1
            self.recursive(i-1 ,j ,grid, ans, move +"U" ,n,vis)
            vis[i-1][j] = 0 # backtrack
            