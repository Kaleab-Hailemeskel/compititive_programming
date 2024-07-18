class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        n = len(s)
        i = 0
        while(i < n):
            ri = int(s[i][-1]) - 1
            if ri != i:
                another_word = s[ri]
                s[ri], s[i] = s[i], s[ri]
            else: 
                s[i] = s[i][:-1]
                i += 1
        return " ".join(s)
