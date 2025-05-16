# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        res = 0
        for i in range(31):
            exponent = (i + 1)
            mod_pow = (1 << exponent)
            pos_number_line = left % mod_pow
            if not(pos_number_line < (mod_pow // 2) or left + (mod_pow - pos_number_line) <= right):
                res |= (1 << i)
        
        return res