class Solution:
    def balancedString(self, s: str) -> int:
        count_s = Counter(s) 
        count_needed = Counter()
        n = len(s)
        each = n // 4
        for key in count_s:
            if count_s[key] > each:
                count_needed[key] = count_s[key] - each
        if not count_needed:
            return 0
        window = Counter()
        
        l = 0
        min_substring = n + 1
        for r in range(n):
            if s[r] in count_needed:
                window[ s[r] ] += 1
            while count_needed <= window and l <= r:
                
                min_substring = min(min_substring, r - l + 1)
                if s[l] in window:
                    window[ s[l] ] -= 1
                    if not window[ s[l] ]:
                        window.pop( s[l] )
                l += 1
        return min_substring
