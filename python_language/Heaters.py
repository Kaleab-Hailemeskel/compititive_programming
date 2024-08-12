class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        n = len(heaters)
        def binarySearch(key):
            if key <= heaters[0]: return heaters[0] - key
            if key >= heaters[-1]: return key - heaters[-1]
            
            l, r = 0, n - 1
            min_rad = float('inf')
            
            while l <= r:
                mid = (l + r) // 2
                if heaters[mid] > key:
                    r = mid - 1
                elif heaters[mid] < key:
                    l = mid + 1
                else:
                    return 0
                min_rad = min(min_rad, abs(key - heaters[mid]))
            return min_rad
        
        max_rad = 0
        for house in houses:
            rad = binarySearch(house)
            max_rad = max(max_rad, rad)
        return max_rad
