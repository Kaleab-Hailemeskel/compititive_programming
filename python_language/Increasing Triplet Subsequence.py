class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_found = float('inf')
        second_found = float('inf')
        for num in nums:
            if num <= first_found: first_found = num
            elif num <= second_found: second_found = num
            else: return True
        return False
                
