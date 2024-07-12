class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3 or arr[0] >= arr[1] : return False
        else: was_increasing = True 
        
        for i in range(2, n):
            if arr[i - 1] >= arr[i]:
                was_increasing = False
            if not was_increasing and arr[i - 1] <= arr[i]: 
                return False

        return arr[-2] > arr[-1]
        
