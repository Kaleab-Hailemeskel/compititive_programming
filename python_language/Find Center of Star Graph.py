class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        catch = Counter()
        n = len(edges)
        for ele1, ele2 in edges:
            catch[ele1] += 1
            catch[ele2] += 1

        ans = catch.most_common(1)
        
        return ans[0][0]
        
