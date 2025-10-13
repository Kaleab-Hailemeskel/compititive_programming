# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count_pair = [0] * k
        for num in arr:
            count_pair[num % k] += 1

        if k % 2 == 0 and count_pair[0] % 2:
            return False
        
        for i in range(1, k):
            if count_pair[i] != count_pair[(-i) % k]:
                return False
        return True