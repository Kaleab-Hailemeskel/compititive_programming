# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for val in arr:
            prefix_xor.append(prefix_xor[-1] ^ val)
        print(prefix_xor)
        res = []
        for fr, to in queries:
            res.append(prefix_xor[fr] ^ prefix_xor[to + 1])
        return res
