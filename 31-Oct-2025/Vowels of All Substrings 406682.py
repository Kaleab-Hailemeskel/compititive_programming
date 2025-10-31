# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        
        n = len(word)
        for i, val in enumerate(word):
            if val in 'aeiou':
                res += (i + 1) * (n - i)
        
        return res