class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        n = len(nums)
        for left in range(n):
            if nums[left] > 0: break
            elif left > 0 and nums[left] == nums[left - 1]:
                continue
            mid, right = left + 1, n - 1
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if not total:
                    arr.append([nums[left], nums[mid], nums[right]])
                    mid, right = mid + 1, right - 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while right > mid and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    mid += 1
                else:
                    right -= 1
        return arr
                    
