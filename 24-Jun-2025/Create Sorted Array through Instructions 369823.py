# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, inst: List[int]) -> int:
        self.res = 0
        self.to_left = [0] * len(inst)
        self.to_right = [0] * len(inst)
        new_inst = [(val, orginal_index) for orginal_index, val in enumerate(inst)]
       
        def merge(arr, low, mid, high):
            merge_arr = []
            i, j = low, mid
            while i < mid or j < high:
    
                if (i < mid and j >= high) or ((i < mid and j < high) and (arr[i] < arr[j])):
                    merge_arr.append(arr[i])
                    i += 1
                elif (i >= mid and j < high) or (((i < mid and j < high)) and arr[i] >= arr[j]):
                    merge_arr.append(arr[j])
                    left_most_index_of_left_arr = bisect_left(inst, inst[j], low, mid)
                    right_most_index_of_left_arr = bisect_right(inst, inst[j], low, mid)
        
                    self.to_right[arr[j][1]] += (mid - right_most_index_of_left_arr)
                    self.to_left[arr[j][1]] += (left_most_index_of_left_arr - low)
            
                    j += 1

            for i in range(low, high):
                arr[i] = merge_arr[i - low]
                inst[i] = merge_arr[i - low][0]
            
        def merge_sort(arr, low, high):
            mid = (high + low) // 2
            if low + 2 >= high:
                merge(arr, low, mid, high)
                return
            
            merge_sort(arr, low, mid)
            merge_sort(arr, mid, high)
            merge(arr, low, mid, high)
        
        merge_sort(new_inst, 0, len(inst))
      
        return sum(min(to_right_ele, to_left_ele) for to_right_ele, to_left_ele in zip(self.to_right, self.to_left)) % (10 ** 9 + 7)
        