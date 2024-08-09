class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def count_ans(c, ans, k):
            max_count = 0
            other = 0
            j = 0
            for i in range(len(ans)):
                if ans[i] != c: other += 1
                while other > k:
                    if ans[j] != c: other -= 1
                    j += 1
                max_count = max(max_count, i - j + 1)
            return max_count
        
        return max(count_ans('T', answerKey, k), count_ans('F', answerKey, k))
