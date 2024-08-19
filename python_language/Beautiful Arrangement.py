class Solution:
    def countArrangement(self, n: int) -> int:
        def check(perm_set, curr_ind):
            if len(perm_set) == n:    return 1
            count = 0
          
            for num in range(1, n + 1):
                if num in perm_set:  continue
                if not(num % curr_ind) or not(curr_ind % num):
                    perm_set.add(num)
                    count += check(perm_set, curr_ind + 1)
                    perm_set.remove(num)
                  
            return count
        return check(set(), 1)
                
                
                
