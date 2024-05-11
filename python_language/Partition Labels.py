class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i

        size, end = 0, lastIndex[s[0]]
        partitions = []
        for i in range(len(s)):
            size += 1
            if lastIndex[s[i]] > end:
                end = lastIndex[s[i]]

            if i == end:
                partitions.append(size)
                size = 0

        return partitions
