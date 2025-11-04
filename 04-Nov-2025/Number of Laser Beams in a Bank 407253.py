# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last_count = 0
        res = 0
        
        for num in bank:    
            n = num.count('1')
            res += last_count * n
            if n != 0:
                last_count = n
        
        return res


