class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        bi_search = []
        n = len(intervals)
        for i in range(n):
            bi_search.append((intervals[i][0], i))
        bi_search.sort()
        def bi(key):
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                if bi_search[m][0] < key:
                    l = m + 1
                elif bi_search[m][0] > key:
                    r = m - 1
                else:
                    return bi_search[m][1]
            return bi_search[l][1] if l < n else bi_search[l - 1][1]
        
        ans = [-1] * n
        for i in range(n):
            j = bi(intervals[i][1])
            if intervals[j][0] >= intervals[i][1]:
                ans[i] = j
        return ans
