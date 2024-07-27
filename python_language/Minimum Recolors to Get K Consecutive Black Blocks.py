class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        count_b = 0
        for i in range(k):
            if blocks[i] == "B":
                count_b += 1
        
        if count_b >= k:
            return 0
        max_b = count_b
        for i in range(k, n):
            l = i - k
            if blocks[l] == "B":
                count_b -= 1
            if blocks[i] == "B":
                count_b += 1
                max_b = max(max_b, count_b)
              
        return k - max_b
        
