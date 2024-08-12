class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def dfs(index, prev):
            if index == n:
                return True
            for j in range(index, n):
                val = int(s[index: j + 1])
                if prev - val == 1 and dfs(j + 1, val):
                    return True
            return False
        for i in range(n - 1):
            val = int(s[ : (i + 1)])
            if dfs(i + 1, val): return True
            
