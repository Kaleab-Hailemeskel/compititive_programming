class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        n = len(arr1)
        unique_ele2 = set(arr2)
        unique_ele1 = set()
        ans = []      
        
        for key in count:
            unique_ele1.add(key)
            
        left_out = unique_ele1.difference(unique_ele2)
        left_out = list(left_out)
        left_out.sort()
        
        for key in arr2:
            ans += [key for _ in range(count[key])]
        for key in left_out:
            ans += [key for _ in range(count[key])]
        return ans
