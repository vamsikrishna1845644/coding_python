class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.recursive(board)
    def recursive(self , board):
        n= len(board)
        for i in range(0,n):
            for j in range(0, n):

                # for the first empty box
                if board[i][j] == '.':
                    # check for all possible numbers in that box
                    for c in map(str , range(1,10)): # we can aslo use ordinal and charecter fucntions i.e (chr(),ord())
                        # chek if that number valid in the board
                        if (self.valid( board ,i , j , c)):
                            # put it in board
                            board[i][j] = c
                            # check for next numbers
                            # and finally after all filling  number combos for that number  if its valid return true
                            if (self.recursive(board) == True):
                                return True
                            else :
                                # we didnot find answer by choosing that number
                                # now back track and check other combinations
                                board[i][j] = '.'
                    return False # no valid number can be placed
        return True # board is already filled
    def valid(self , board , row , col , c):
        # to check if that particular nuber is valid in  the board
        # loop for row , col , and 3*3 grid 

        for  i  in range(0,9):

            # col
            if board[row][i] == c:
                return False # not a valid number
            
            # row

            if board[i][col] == c:
                return False
            
            # 3*3 grid

            if board[3*(row//3) + i//3][ 3*(col//3) + i%3] == c:
                return False
        return True
            



                            
