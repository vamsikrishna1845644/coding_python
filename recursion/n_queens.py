class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = [ ] # list to store ans 
        board = [ ['.']*n for _ in range(n)] # board temparrory # dont foregt to multiply with n
        lrow = [0]*n # left row checking list
        ldia = [0]*(2*(n-1)) # left diagonal checking list
        udia = [0]*(2*(n-1)) # upper diagonal checking list
        self.recursive(0, board , ans , lrow , ldia , udia , n)
        return ans 
    def recursive(self ,col, board , ans , lrow , ldia , udia , n ):
        # base case 
        if col == n :
           # ans.append(board[:,:]) #append snapshort of the board
           # i made a msitake here i confused syntax of numpy arryas to pyhton lists
           snapshot = ["".join(row) for row in board]
           ans.append(snapshot)
           return
        
        # check for each row 
        for row  in range(0,n):
            # only when the queen can be placed in the particular row
            if lrow[row] == 0 and ldia[row + col ] == 0 and udia[n-1+col - row ] == 0:
                board[row][col] = 'Q' # put queen 
                # update the checking lists
                lrow[row] = 1
                ldia[row+col] = 1
                udia[ n-1 + col - row] = 1
                # check all the other paths form there
                self.recursive(col+1, board , ans , lrow , ldia , udia , n )
                # make sure to remove the thing while backtracking
                board[row][col] = '.'
                lrow[row] = 0
                ldia[row+col] = 0
                udia[ n-1 + col - row] = 0
