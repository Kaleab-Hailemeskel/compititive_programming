class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: return 0
        ans = 0
        each_num = Counter()
        curr_num = abs(num)
        while(curr_num > 0):
            index = (curr_num % 10)
            each_num[index] += 1
            curr_num //= 10
        
        if num > 0:
            for i in range(1, 10):
                if i in each_num:
                    ans += int(i)
                    each_num[i] -= 1
                    break
            for i in range(10):
                while i in each_num and each_num[i] > 0:
                    ans *= 10
                    ans += int(i)
                    each_num[i] -= 1
            return ans
        
        else:
            for i in range(9, -1, -1):
                while each_num[i]:
                    ans *= 10
                    ans += int(i)
                    each_num[i] -= 1          
            return -ans
            
            
