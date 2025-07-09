# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_arr = 0
        # 10 ** 9 ~= 2 ** 30
        N = 31
        count = num2.bit_count()
        res = 0
        # from the front
        for i in range(N):
            rev = N - i - 1
            if num1 & (1 << rev) and count:
                count -= 1
                res ^= (1 << rev)
        i = 0
        while count:
            if res & (1 << i) == 0:
                res ^= 1 << i
                count -= 1
            i += 1
        
        return res




