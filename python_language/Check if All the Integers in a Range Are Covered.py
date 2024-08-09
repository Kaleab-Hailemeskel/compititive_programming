class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = set(range(left, right + 1))
        for i in range(len(ranges)):
            l, r = ranges[i][0], ranges[i][1]
            cover -= set(range(l, r + 1))
        return not cover
