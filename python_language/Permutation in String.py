class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sizeOfs1 = len(s1)
        sizeOfs2 = len(s2)
        s1Dict = collections.Counter(s1)
        s2Dict = collections.Counter(s2[:min(sizeOfs2, sizeOfs1 - 1)])
        for right in range(sizeOfs1 - 1, sizeOfs2):
            s2Dict[s2[right]] = 1 + s2Dict.get(s2[right], 0)
            if s2Dict == s1Dict:
                return True
            
            s2Dict[s2[right - (sizeOfs1 - 1)]] -= 1
            if s2Dict[s2[right - (sizeOfs1 - 1)]] == 0:
                del  s2Dict[s2[right - (sizeOfs1 - 1)]]
            
        return False
