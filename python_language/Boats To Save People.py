class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left, right = 0, len(people) - 1

        while left <= right:
            sum_ = people[left] + people[right]
            if sum_ <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            count += 1
                
        return count
