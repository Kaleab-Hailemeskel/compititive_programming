class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        l, n = 0, len(s)
        count_vowel = 0
        max_count = 0
        for r in range(n):
            if s[r] in vowels:
                count_vowel += 1
            if r - l == k:
                if s[l] in vowels:
                    count_vowel -= 1
                l += 1
            max_count = max(count_vowel, max_count)
        
        return max_count
                
