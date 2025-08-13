# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        set_of_parents = defaultdict(set)
        for parent, child in pre:
            set_of_parents[child].add(parent)
        res = []
        for p, c in queries:
            stack = [c]
            vis = set(stack)
            while stack and p not in set_of_parents[stack[-1]]:
                curr_c = stack.pop()
                for each_parent in set_of_parents[curr_c]:
                    if each_parent not in vis:
                        vis.add(each_parent)
                        stack.append(each_parent)            
            if stack and p in set_of_parents[stack[-1]]:
                res.append(True)
            else:
                res.append(False)
        return res
                    



        