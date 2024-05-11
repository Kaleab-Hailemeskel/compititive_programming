class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        left = 0
        maxLength = 0
        maxCountOfChars = 0
        arr = [0] * 26
        for right in range(0, size):
            arr[ord(s[right]) - ord('A')] += 1
            maxCountOfChars = max(maxCountOfChars, arr[ord(s[right]) - ord('A')])
            while (right - left + 1) - maxCountOfChars > k:
                arr[ord(s[left]) - ord('A')] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
