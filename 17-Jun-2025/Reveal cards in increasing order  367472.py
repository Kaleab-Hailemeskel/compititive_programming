# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        qeue = deque(range(len(deck)))
        deck.sort()
        ans = [0] * len(deck)
        for n in deck:
            i = qeue.popleft()
            ans[i] = n
            
            if qeue:
                qeue.append(qeue.popleft())
        return ans
        