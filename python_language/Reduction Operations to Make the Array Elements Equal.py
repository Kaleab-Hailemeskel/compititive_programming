# my Solution
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        arr = []
        for key in num_count:
            arr.append(key)
        arr.sort()        
        ans = 0
        n = len(arr)
        tot_convert = 0
        print(arr)
        for i in range(n - 1):
            num = arr[n - 1 - i]
            tot_convert += num_count[num]
            ans += tot_convert
        return ans

# Leet codes Solution
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        up = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up += 1
            ans += up
        
        return ans
