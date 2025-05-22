# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        index_bit = defaultdict(int)
        for index, val in enumerate(s):
            if val.isalpha():
                index_bit[len(index_bit)] = index
        
        s_list = list(s)
        res = []
        if not index_bit: 
            return [s]

        for num in range((1 << (len(index_bit)))):
            copy_ = s_list[:]
            for i in range(len(index_bit)):
                if not (num & (1 << i)):
                    list_index = index_bit[i]
                    copy_[list_index] = copy_[list_index].swapcase()
            res.append(''.join(copy_))
        
        return res


