class Solution:
    def dailyTemperatures(self, te: List[int]) -> List[int]:
        q = []
        curr_max = 0
        ans = [0] * len(te)
        i, n = 0, len(te)
        
        while i < n:
            while q and q[-1][0] < te[i]:
                j =  q[-1][1]
                ans[j] = i - j
                q.pop()    
            q.append([te[i], i])
            i += 1
        
        return ans
                
            
