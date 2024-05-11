class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        sizeOfP = len(p)
        sizeOfS = len(s)
        pDictionary = {}
        sDictionary = {}

        for i in range(0, sizeOfP):
            if pDictionary.get(p[i]):
                pDictionary[p[i]] += 1
            else:
                pDictionary[p[i]] = 1
        for i in range(0, min(sizeOfS, sizeOfP - 1)):
            if sDictionary.get(s[i]):
                sDictionary[s[i]] += 1
            else:
                sDictionary[s[i]] = 1

        for i in range(sizeOfP - 1, sizeOfS):
            curr_char = s[i]
            if sDictionary.get(curr_char):
                sDictionary[curr_char] += 1
            else:
                sDictionary[curr_char] = 1
            if pDictionary == sDictionary:
                ans.append(i - (sizeOfP - 1))
            sDictionary[s[i - (sizeOfP - 1)]] -= 1
            if sDictionary[s[i - (sizeOfP - 1)]] == 0:
                del sDictionary[s[i - (sizeOfP - 1)]]

        return ans
