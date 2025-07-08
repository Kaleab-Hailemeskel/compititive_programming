# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

# says TLE but other solution with the same complexity was working for others
class Solution:
    def solveSudoku(self, main: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(row, col):
            if col == 9:
                row += 1
                col = 0

            if row == 9:
                return True

            if main[row][col] == '.':
                for num in range(1, 10):
                    if is_valid(row, col, f'{num}'):
                        main[row][col] = f'{num}'
                        # print(row, col, 'is set to', num)
                        if backtrack(row, col + 1):
                            return True
                        main[row][col] = '.'
                return False
            return backtrack(row, col + 1)
                            

        def is_valid(row, col, num):
            # print('is_valid')
            for i in range(9):
                # check row and col 
                if main[row][i] == num or main[i][col] == num:
                    return False
                # check 3 x 3 grid
                if main[3*(row//3) + i//3][3*(col//3) + i%3] == num:
                    return False
        
            return True

        backtrack(0, 0)
