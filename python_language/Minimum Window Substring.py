########### Original Solution ##########
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        t_dict = collections.Counter(t)
        s_dict = collections.Counter()
        min_window, min_word = 10**5 + 1, [-1, -1]
        j = 0
        for i, ch in enumerate(s):
            s_dict[ch] += 1
            while s_dict > t_dict and j <= i and (s[j] not in t_dict or s_dict[s[j]] - 1 >= t_dict[s[j]]):
            
                s_dict[s[j]] -= 1
                j += 1
            
            if s_dict >= t_dict and min_window > i - j + 1:
                min_window = i - j + 1
                min_word = [j, i]
        
        l, r  = min_word
        
        return s[l: r + 1] if min_window != 10**5 + 1 else ""

######### Efficient Solution ##########
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        t_dict = collections.Counter(t)
        s_dict = collections.Counter()
        min_window, min_word = float('inf'), [-1, -1]
        have, need = 0, len(t_dict)
        j = 0
        
        for i, ch in enumerate(s):
            s_dict[ch] += 1
            if ch in t_dict and t_dict[ch] == s_dict[ch]:
                have += 1
            
            while have == need:
                if (i - j + 1) < min_window:
                    min_window = i - j + 1
                    min_word = [j , i]
                s_dict[s[j]] -= 1
                if s[j] in t_dict and s_dict[s[j]] < t_dict[s[j]]:
                    have -= 1
                j += 1
        l, r = min_word
        return s[l: r+1] if min_window != float('inf') else ""
                
                    
        
            
        
            
