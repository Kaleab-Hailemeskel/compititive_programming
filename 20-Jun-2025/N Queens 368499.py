# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Proudly Submitted \U0001f600
        
        # some refinements at the return 
        row_set = set()
        col_set = set()
        diagonal_right = set()
        diagonal_left = set()
        
        final_res = []

        def recur(row, col, remain):
            if row in row_set or col in col_set or row - col in diagonal_right or row + col in diagonal_left:
                return 0
            
            remain -= 1

            if remain == 0:
                final_res.append([(['.'] * n) for _ in range(n)])
                new_table = final_res[-1]
                new_table[row][col] = 'Q'
                return 1

            row_set.add(row)
            col_set.add(col)
            diagonal_right.add(row - col)
            diagonal_left.add(row + col)
            
            valid_count = 0
            next_row = row + 1
            if next_row < n:
                for new_col in range(n):
                    valid_count += recur(next_row, new_col, remain)
            
            for last_ele_index in range(-1, -valid_count - 1, -1):
                new_table = final_res[last_ele_index]
                new_table[row][col] = 'Q'
                    
            

            row_set.remove(row)
            col_set.remove(col)
            diagonal_right.remove(row - col)
            diagonal_left.remove(row + col)

            return valid_count

        max_res = 0
        for col in range(n):
            valid_count = recur(0, col, n)
            for last_ele_index in range(-1, -valid_count - 1, -1):
                new_table = final_res[last_ele_index]
                new_table[0][col] = 'Q'
        
        
       
        return tuple(set(tuple(''.join(each_row) for each_row in each_table) for each_table in final_res))
       