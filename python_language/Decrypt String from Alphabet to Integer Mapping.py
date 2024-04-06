class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        size = len(s)
        i = 0
        while i < size:
            if i + 2 < size and s[i + 2] == '#':
                ans += chr(96 + int(s[i:i + 2]))
                i += 3
            else:
                ans += chr(96 + int(s[i:i + 1]))
                i += 1

        return ans
                
