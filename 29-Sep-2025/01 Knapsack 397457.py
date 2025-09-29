# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        size, weight_capacity = len(val), W
        weight_value_list = []
        WEIGHT, VALUE = 0, 1

        weight_value_list = [ (weight, value) for weight, value in zip(wt, val)]                   
        dp = [[-1] * (size + 1) for _ in range(weight_capacity + 1)]
           
        stack = [(0, 0)]
        
        while stack:
            cumulative_weight, choosing_index = stack.pop()
            if choosing_index >= len(weight_value_list):
                dp[cumulative_weight][choosing_index] = 0
                continue
            
            if dp[cumulative_weight][choosing_index] == -1:
                curr_weight = cumulative_weight + weight_value_list[choosing_index][WEIGHT]
    
                include_curr_item = 0
                if curr_weight <= weight_capacity:
                    if dp[curr_weight][choosing_index + 1] == -1:
                        stack.append((cumulative_weight, choosing_index))
                        stack.append((curr_weight, choosing_index + 1))
                        continue
                    include_curr_item = dp[curr_weight][choosing_index + 1] + weight_value_list[choosing_index][VALUE]
                
                if dp[cumulative_weight][choosing_index + 1] == -1:
                    stack.append((cumulative_weight, choosing_index))
                    stack.append((cumulative_weight, choosing_index + 1))    
                    continue
                exclude_curr_item = dp[cumulative_weight][choosing_index + 1]
                
                            
                dp[cumulative_weight][choosing_index] = max(include_curr_item, exclude_curr_item)   
        
        
        return dp[0][0]