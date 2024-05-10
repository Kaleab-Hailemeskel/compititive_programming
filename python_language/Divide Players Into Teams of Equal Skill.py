class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort() 
        target = skill[0] + skill[-1]
        value = 0
        l, r = 0, len(skill) - 1
        while l < r:
            if skill[l] + skill[r] == target:
                value += (skill[l] * skill[r])
            else:
                return -1
            l += 1
            r -= 1
        return value
        
        
        
