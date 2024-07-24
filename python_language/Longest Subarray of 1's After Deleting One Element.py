# solution 1
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        longest_window = 0
        start = 0
        for i in range(len(nums)):
            zero_count += (nums[i] == 0)
            while zero_count > 1:
                zero_count -= (nums[start] == 0)
                start += 1
            longest_window = max(longest_window, i - start)
        return longest_window

# solution 2
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_now = [0] * 2
        max_1 = 0
        n = len(nums)
        for i in range(n):
            if not nums[i]:
                prev_now[0] = prev_now[1]
                prev_now[1] = 0
            else:
                prev_now[1] += 1
            max_1 = max(max_1, sum(prev_now))
        return max_1 - 1 if max_1 == n else max_1
