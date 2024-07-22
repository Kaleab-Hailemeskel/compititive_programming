class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        max_time_taken = 0
        pn = len(processorTime)
        tn = len(tasks)
        for pi in range(pn):
            ti = int(tn - (1 + 4 * pi))
            max_time_taken = max(max_time_taken, tasks[ti] + processorTime[pi])
        
        return max_time_taken
