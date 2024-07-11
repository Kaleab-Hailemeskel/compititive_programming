class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        occ = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.' and (f"{i} row {val}" in occ or f"{j} col {val}" in occ or f"{int(i/3)} {int(j/3)} sub_box {val}" in occ):
                    print(occ)
                    return False
                else:
                    occ.add(f"{i} row {val}")                   
                    occ.add(f"{j} col {val}")
                    occ.add(f"{int(i/3)} {int(j/3)} sub_box {val}")

        return True
                
                
