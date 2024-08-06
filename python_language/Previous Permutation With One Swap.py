class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i >= 0:
            max_ = i + 1
            for j in range(max_ + 1, len(arr)):
                if arr[max_] < arr[j] < arr[i]:
                    max_ = j
            arr[max_], arr[i] = arr[i], arr[max_]
        return arr

            
