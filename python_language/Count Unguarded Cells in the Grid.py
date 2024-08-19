class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cell = [["" for _ in range(n)] for _ in range(m)]
        for guard in guards:
            cell[guard[0]][guard[1]] = "G"

        for wall in walls:
            cell[wall[0]][wall[1]] = "W"
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for guard in guards:
            for row_dir, col_dir in direction:
                row, col = guard[0] + row_dir, guard[1] + col_dir

                while 0 <= row < m and 0 <= col < n and cell[row][col] not in ("G", "W"):
                    cell[row][col] = "g"
                    row += row_dir
                    col += col_dir
                    
        count_ung = 0
        for i in range(m):
            for j in range(n):
                if not cell[i][j]: count_ung += 1

        return count_ung
