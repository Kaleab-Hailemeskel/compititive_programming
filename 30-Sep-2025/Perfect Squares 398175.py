# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        for square in map(lambda a: a * a, range(1, 102)):
            if square <= n:
                perfect_squares.append(square)
            else:
                break
        # print(perfect_squares)
        memo = [float('inf')] * (n + 1)
        memo[0] = 0
        for each_square in perfect_squares:
            for each_n in range(1, n + 1):
                wanted_n = each_n - each_square
                if wanted_n >= 0:
                    memo[each_n] =  min(
                        memo[each_n],
                        memo[wanted_n] + 1
                    )
        return memo[n] if memo[n] != float('inf') else 0
