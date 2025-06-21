# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def __init__(self):
        self.final_res = 0
    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        return self.final_res

    def mergeSort(self, arr):
        len_ = len(arr)
        half = math.ceil(len_ / 2)
        if len_ < 2:
            return self.merge(arr, [])

        return self.merge(self.mergeSort(arr[:half]), self.mergeSort(arr[half:]))
        
    def merge(self, arr1, arr2):   
        last_left = 0
        res = 0
        for index, val in enumerate(arr1):
            while last_left < len(arr2) and val <= (arr2[last_left] * 2):
                last_left += 1
            res += (len(arr2) - last_left)
        
        new_arr = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                new_arr.append(arr1[i])
                i += 1
            else:
                new_arr.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            new_arr.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            new_arr.append(arr2[j])
            j += 1
        
        self.final_res += res
        return new_arr