class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        fruitsCount = {}
        maxYield = 0
        for right in range(len(fruits)):
            fruitsCount[fruits[right]] = 1 + fruitsCount.get(fruits[right], 0)

            while len(fruitsCount) > 2:
                fruitsCount[fruits[left]] -= 1
                if fruitsCount[fruits[left]] == 0:
                    del fruitsCount[fruits[left]]
                left += 1

            maxYield = max(maxYield, right - left + 1)

        return maxYield
