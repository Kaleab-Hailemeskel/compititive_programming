class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        ans = []
        for key in count1:
            value = count1[key]
            if key in count2:
                use_count = value if value < count2[key] else count2[key]
                ans += [key for _ in range(use_count)]
                
        return ans
