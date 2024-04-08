class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        smallWord = ''
        minLen = len(words[0])
        smallIndex = 0

        for i in range(len(words)):
            if minLen > len(words[i]):
                smallWord = words[i]
                smallIndex = i
        
        if smallIndex != 0:
            words[smallIndex] = words[0]
            words[0] = smallWord


        word = words[0]
        answer = []
        for j in word:
            check = True
            for i in range(1, len(words)):
                if j not in words[i]:
                    check = False
                    break
                else:
                    words[i] = words[i].replace(j, '',  1)
            if check:
                answer.append(j)
        return answer
