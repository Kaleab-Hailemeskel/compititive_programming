class Solution:
        def maximumUniqueSubarray(self, nums: List[int]) -> int:
            n = len(nums)
            l = 0
            unique = set()
            _sum, max_sum = 0, 0

            for r in range(n):
                if not nums[r] in unique:
                    unique.add(nums[r])
                    _sum += nums[r]    
                else:
                    while nums[l] != nums[r] and l <= r:
                        _sum -= nums[l]
                        unique.remove(nums[l])
                        l += 1
                    l += 1

                max_sum = max(max_sum, _sum)

            return max_sum
