class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        index = 0
        n = len(tickets)
        while tickets[k] != 0:
            
            if tickets[index % n] == 0:
                index += 1
                continue
            
            tickets[index % n] -= 1
            count += 1
            index += 1
        
        return count
