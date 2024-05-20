class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in range(len(s)):
            if s[i] in close_open:
                if not stack or stack.pop() != close_open[s[i]]:
                    return False
            else:
                stack.append(s[i])

        return True if not stack else False
