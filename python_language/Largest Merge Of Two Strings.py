class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        construct = []
        i1 = i2 = 0
        s1 = len(word1)
        s2 = len(word2)
        while i1 < s1 and i2 < s2:
            if (word1[i1] < word2[i2]):
                construct.append(word2[i2])
                i2 += 1

            elif word1[i1] == word2[i2]:
                if word1[i1:] <= word2[i2:]:
                    construct.append(word2[i2])
                    i2 += 1
                else:
                    construct.append(word1[i1])
                    i1 += 1
            else:
                construct.append(word1[i1])
                i1 += 1

        if i2 < s2:
            construct.append(word2[i2:])
        if i1 < s1:
            construct.append(word1[i1:])

        return "".join(construct)
