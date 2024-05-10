class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left1 = left2 = 0
        size1, size2 = len(nums1), len(nums2)
        while left1 < size1 and left2 < size2:
            if nums1[left1] < nums2[left2]:
                left1 += 1
            elif nums2[left2] < nums1[left1]:
                left2 += 1
            else:
                return nums1[left1]
        
        return -1
