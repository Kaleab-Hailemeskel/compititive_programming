class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lam = lambda a, b: -1 if a + b > b + a else (1 if a + b < b + a else 0)

        str_num = []
        for i in range(len(nums)):
            str_num.append(str(nums[i]))

        str_num.sort(key = cmp_to_key(lam))

        return str(int("".join(str(num) for num in str_num)))
