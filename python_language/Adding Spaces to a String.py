class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        sstr = len(s)
        sspace = len(spaces)
        j = 0
        for i in range(sstr):
            if j < sspace and spaces[j] == i:
                ans.append(" ")
                j += 1
            ans.append(s[i])
        
        return "".join(ans)
