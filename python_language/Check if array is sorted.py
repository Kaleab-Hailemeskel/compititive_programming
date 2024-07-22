class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        n = len(arr)
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                return False
        return True
