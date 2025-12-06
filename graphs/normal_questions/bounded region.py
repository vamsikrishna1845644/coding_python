class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        vis = [[0]*m for _ in range(n)]
        # using dfs

        # first row adn last row
        for j in range(m):
            # first row
            if not vis[0][j] and board[0][j] == 'O':
                self.dfs(0,j,vis,board)
            # last row
            if not vis[n-1][j] and board[n-1][j] == 'O':
                self.dfs(n-1,j,vis,board)
        # first col adn last col
        for i in range(n):
            # first col
            if not vis[i][0] and board[i][0] == 'O':
                self.dfs(i,0,vis,board)
            # last col
            if not vis[i][m-1] and board[i][m-1] == 'O':
                self.dfs(i,m-1,vis,board)
        
        # check for remaining untoucheds os in the board and make them to x
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not vis[i][j]:
                    board[i][j] = 'X'
       
    def dfs(self,row,col,vis,board):
        # mark it as visted
        vis[row][col] = 1
        n = len(board)
        m = len(board[0])

        # move in 4 directions
        delr = [-1,0,1,0]
        delc = [0,1,0,-1]
        for i in range(4):
            newr = row + delr[i]
            newc = col + delc[i]
            if newr >=0 and newr<n and newc >=0 and newc <m and not vis[newr][newc] and board[newr][newc] == 'O':
                # we go to the dept 
                # mark it 
                vis[newr][newc] = 1
                self.dfs(newr,newc,vis,board)
