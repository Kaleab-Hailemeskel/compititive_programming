class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        right = len(s) - 1
        left = 0
        vowels = {'a' : 1, 'e' : 1, 'i' : 1, 'o' : 1, 'u' : 1}
        while left < right:
            if s[left].lower() in vowels:
                if s[right].lower() in vowels:
                    letter = s[right]
                    s[right] = s[left]
                    s[left] = letter
                    left += 1
                right -= 1
            else:
                left += 1

        return "".join(s)
