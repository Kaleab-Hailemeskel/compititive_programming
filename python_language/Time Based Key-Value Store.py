class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict or timestamp < self.dict[key][0][1]:
            return ""
        n = len(self.dict[key])
        left, right = 0, n - 1
        li = self.dict[key]
        while left <= right:
            mid = (left + right) // 2
            if li[mid][1] < timestamp:
                left = mid + 1
            elif li[mid][1] > timestamp:
                right = mid - 1
            else:
                return li[mid][0]
        
        return li[left - 1][0] if left > 0 else li[left][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
