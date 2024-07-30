class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        nxt_queue = deque()
        nxt_arr = [0] * n
        
        pre_queue = deque()
        pre_arr = [0]  * n
        
        for i in range(n):
            while nxt_queue and arr[nxt_queue[-1]] > arr[i]: # >= is a must between line 11 or line 19, but not on both
                nxt_arr[nxt_queue[-1]] = i - nxt_queue[-1]
                nxt_queue.pop()
            nxt_queue.append(i)
        while nxt_queue:
            i = nxt_queue.pop()
            nxt_arr[i] = n - i
        for i in range(n - 1, -1, -1):
            while pre_queue and arr[pre_queue[-1]] >= arr[i]:
                pre_arr[pre_queue[-1]] = pre_queue[-1] - i
                pre_queue.pop()
            pre_queue.append(i)
        while pre_queue:
            i = pre_queue.pop()
            pre_arr[i] = i + 1
        sol = 0
        for i in range(n):
            sol += (arr[i] * pre_arr[i] * nxt_arr[i])
        
        return (sol % int(pow(10, 9) + 7))
