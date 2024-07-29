class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        window = set()
        min_len = len(cards) + 1
        l = 0
        for r in range(len(cards)):
            while cards[r] in window and l < r:
                min_len = min(min_len, r - l + 1)
                window.remove(cards[l])
                l += 1
            window.add(cards[r])                      
        
        return -1 if min_len == len(cards) + 1 else min_len
                
