class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five , ten, tt = 0, 0, 0
        for i in range(len(bills)):
            if bills[i] == 20:
                tt += 1
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five > 2:  five -= 3
                else: return False
                
            elif bills[i] == 10:   
                ten += 1
                if not five: return False
                else: five -= 1
            else:
                five += 1
        return True
