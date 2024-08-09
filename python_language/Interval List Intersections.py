class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def inter(li_1, li_2) -> List[int]:
            x, y = 0, 0
            x = li_2[0] if li_1[0] < li_2[0] else li_1[0]
            y = li_2[1] if li_2[1] < li_1[1] else li_1[1]
            return [x, y]
        ans = []
        a, b = 0, 0
        left, right = 0, 1
        while a < len(firstList) and b < len(secondList):
            if firstList[a][left] <= secondList[b][left] <= firstList[a][right] or firstList[a][left] <= secondList[b][right] <= firstList[a][right]:
                ans.append(inter(firstList[a], secondList[b]).copy())                   
            
            elif secondList[b][left] <= firstList[a][left] <= secondList[b][right] or secondList[b][left] <= firstList[a][right] <= secondList[b][right]:
                ans.append(inter(firstList[a], secondList[b]).copy())
            
            if firstList[a][right] > secondList[b][right]:
                b += 1
            elif firstList[a][right] < secondList[b][right]:
                a += 1
            else:
                b += 1
                a += 1  
        return ans
####### same implementation but nice way of writting #########
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
         
        result = []
        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]
            if a_start <= b_end and b_start <= a_end:                       # Criss-cross lock
                result.append([max(a_start, b_start), min(a_end, b_end)])   # Squeezing
                 
            if a_end <= b_end:         # Exhausted this range in A
                i += 1               # Point to next range in A
            else:                      # Exhausted this range in B
                j += 1               # Point to next range in B
        return result
