# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        for i in range(n - 2, -1, -1):
            point, br_power = questions[i]
            next_i = i + br_power + 1
            if next_i < n:
                questions[i][0] += questions[next_i][0]
            if questions[i][0] < questions[i + 1][0]:
                questions[i] = questions[i + 1]
        
        return questions[0][0]
