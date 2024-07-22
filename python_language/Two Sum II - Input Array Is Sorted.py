class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        lt, rt = 0, n - 1
        while lt < rt and numbers[lt] + numbers[rt] != target:
            if numbers[lt] + numbers[rt] < target:
                lt += 1
            else:
                rt -= 1
        
        return [lt + 1, rt + 1]
