class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square_holder = {0:0}
        a = 0
        while a * a <= c:
            if c - (a * a) in square_holder:
                return True
            a += 1
            square_holder[a * a] = a

        return False
