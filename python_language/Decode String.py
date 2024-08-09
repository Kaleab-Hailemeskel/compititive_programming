class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                str_ = ""
                while stack[-1] != "[":
                    str_ = stack.pop() + str_
                stack.pop()
                k = ""
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                
                stack.append(int(k) * str_)
        
        return "".join(stack)
            
                
            
