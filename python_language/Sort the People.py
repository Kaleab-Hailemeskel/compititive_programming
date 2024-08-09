class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_p = defaultdict(int)
        for i in range(len(names)):
            sorted_p[heights[i]] = names[i]
        
        heights.sort(reverse = True)
        ans = [" "] * len(heights)
        for i in range(len(heights)):
            ans[i] = sorted_p[heights[i]]
        
        return ans
