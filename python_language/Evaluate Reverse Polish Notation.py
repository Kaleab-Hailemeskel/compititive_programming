class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ope = set(["*", "/", "+", "-"])  
        num = []
        for val in tokens:
            if val in ope:
                l = num.pop()
                f = num.pop()
                if val == "+":
                    num.append(l + f)
                elif val == "-":
                    num.append(f - l)
                elif val == "/":
                    f = math.ceil(f/l) if f/l < 0 else math.floor(f/l)
                    num.append(f)
                else:
                    ans = f * l
                    num.append(ans)
            else:
                num.append(int(val))

        return num[0]
