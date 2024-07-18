class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n_flip = len(flips)
        after_bound = set()
        count_zero_before_bound = 0
        count_ans = 0
        for i in range(n_flip):
            rl = flips[i] - 1
            if rl > i:
                after_bound.add(rl)
                if not i in after_bound:
                    count_zero_before_bound += 1
            elif rl < i and i in after_bound:
                count_zero_before_bound -= 1

            if count_zero_before_bound == 0:
                count_ans += 1
        
        return count_ans
