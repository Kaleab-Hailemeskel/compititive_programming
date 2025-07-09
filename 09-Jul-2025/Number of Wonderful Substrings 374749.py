# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        give_corr_index = lambda x: ord(x) - ord('a')
        count_occ = Counter([0])
        
        def count_wonderful( num ):
            res = count_occ[num]
            for i in range(10):
                wanted_num = num ^ (1 << i)
                res += count_occ[wanted_num]
            
            return res

        curr_sum = 0
        res = 0
        
        for ch in word:
            curr_sum ^= (1 << give_corr_index(ch))         
            res += count_wonderful(curr_sum)
            count_occ[curr_sum] += 1
        
        return res



