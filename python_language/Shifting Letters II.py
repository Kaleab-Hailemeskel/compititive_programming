class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_sum = [0] * (n + 1)
        di = [-1, 1]
        for i, j , k in shifts:
            prefix_sum[i] += di[k]
            prefix_sum[j + 1] -= di[k]
        for i in range(1, n + 1):
            prefix_sum[i] += prefix_sum[i - 1]
        
        s = list(s)
        for i in range(n):
            s[i] = chr((( ord(s[i]) - ord('a') + prefix_sum[i]) % 26) + ord('a'))
        
        return "".join(s)
