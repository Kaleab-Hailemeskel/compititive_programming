class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        n, m = len(name), len(typed)
        last_char = '1'
        while i < n and j < m:
            if name[i] == typed[j]:
                last_char = name[i]
                i += 1
                j += 1
            elif typed[j] == last_char:
                j += 1
            else:
                return False
        while j < m:
            if typed[j] != last_char:
                return False
            j += 1
        return False if i < n else True

