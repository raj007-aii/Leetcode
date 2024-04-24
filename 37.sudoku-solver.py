#
# @lc app=leetcode id=37 lang=python
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, num):
            # Check if the number already exists in the same row or column
            for i in range(9):
                if board[i][col] == num or board[row][i] == num:
                    return False
            
            # Check if the number already exists in the 3x3 subgrid
            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == num:
                        return False
            
            return True

        def backtrack():
            for row in range(9):
                for col in range(9):
                    # If the cell is empty
                    if board[row][col] == '.':
                        # Try placing each digit from '1' to '9'
                        for num in map(str, range(1, 10)):
                            if isValid(row, col, num):
                                board[row][col] = num
                                # Recursively call backtrack for the next cell
                                if backtrack():
                                    return True
                                # If no solution is found, backtrack and try the next digit
                                board[row][col] = '.'
                        return False
            return True

        backtrack()
        
# @lc code=end

