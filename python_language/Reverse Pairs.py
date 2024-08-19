class Solution:
    def reversePairs(self, nums):
        def merge_sort(arr, low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            count = merge_sort(arr, low, mid) + merge_sort(arr, mid + 1, high)
            count += merge(arr, low, mid, high)
            return count

        def merge(arr, low, mid, high):
            temp = [0] * (high - low + 1)
            l_size, r_size = mid - low + 1, high - mid
            i, j = low, mid + 1
            count = 0

            while i <= mid and j <= high:
                if arr[i] > 2 * arr[j]:
                    count += mid - i + 1
                    j += 1
                else:
                    i += 1
            i, j = low, mid + 1
            k = 0
            while i <= mid and j < r_size + mid + 1:
                if arr[i] <= arr[j]: 
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1
            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j < r_size + mid + 1:
                temp[k] = arr[j]
                k += 1
                j += 1
            k = low
            for i in range(len(temp)):
                arr[k + i] = temp[i]
            
            return count
        return merge_sort(nums, 0, len(nums) - 1)
