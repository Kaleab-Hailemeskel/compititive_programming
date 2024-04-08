class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        size = len(arr)
        ans = []
        currIndex = size - 1
        for i in range(0, size):
            if arr[currIndex] == (currIndex + 1):
                currIndex -= 1
                continue
            indexOfToBeCurr = arr.index(currIndex + 1)
            if indexOfToBeCurr != 0:
                ans.append( (indexOfToBeCurr + 1) )
                arr[0: indexOfToBeCurr + 1] = arr[indexOfToBeCurr - size::-1]
            ans.append( arr[0] )
            arr[0: arr[0]] = arr[arr[0] - 1 - size::-1]
            currIndex -= 1
        return ans
