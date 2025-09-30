# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        pyramid = [[0] * size for size in range(1, query_row + 2)]
        pyramid[0][0] = poured
        for row in range(query_row):
            for col in range(row + 1):
                if pyramid[row][col] > 1:
                    exece = pyramid[row][col] - 1
                    pyramid[row + 1][col] += exece / 2
                    pyramid[row + 1][col + 1] += exece / 2
                    # pyramid[row][col] = 1
        # for row in pyramid:
        #     print(row)

        # if the glass if more than full, which is there is no such thing we need to limit the max to 1
        return min(1, pyramid[-1][query_glass])

