class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_str = ""
        for j in range(1, len(strs[0]) + 1):
            same = strs[0][:j]
            i = 0
            while i < len(strs):
                if j > len(strs[i]):
                    break
                if strs[i][:j] != same:
                    break
                i += 1
            if i >= len(strs):
                longest_str = same
            else:
                break
        return longest_str
