class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c
        n = len(new_s)
        for i in range(n//2):
            if new_s[i] != new_s[~i]:
                return False
        return True
