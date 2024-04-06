class Solution:
    def similarPairs(self, words: List[str]) -> int:
        keyvalarr = []
        for j in range(0, len(words)):
            keyVal = {}
            for i in range(0, len(words[j])):
                keyVal[words[j][i]] = 1
            keyvalarr.append(keyVal)
        ansCount = 0
        for index in range(0, len(keyvalarr)):
            for anIndex in range( index + 1, len(keyvalarr)):
                if keyvalarr[index] == keyvalarr[anIndex]:
                    ansCount += 1

        return ansCount
       
    
    
    
    
    
    
    
