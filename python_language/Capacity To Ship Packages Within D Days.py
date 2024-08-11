class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(cap):
            count_day = 0
            sumw = weights[0]
            for i in range(1, len(weights)):
                if sumw + weights[i] > cap:
                    count_day += 1
                    sumw = 0
                sumw += weights[i]

            return count_day < days
              
        right = sum(weights) # max capacity OR the capacity to delever the package within one day
        left = max(weights)

        res = right
        while left <= right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1

        return res
