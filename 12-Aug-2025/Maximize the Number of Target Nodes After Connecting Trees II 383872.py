# Problem: Maximize the Number of Target Nodes After Connecting Trees II - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution:
    def createGraph_ReturnTheNodeWithMostChildren(self, graph: defaultdict(list),edges: list[int]) -> int:
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        many_children_parent = 0
        for parent, children_list in graph.items():
            if len(children_list) > len(graph[many_children_parent]):
                many_children_parent = parent
        return many_children_parent
    def countMaxOccOfSubSeq(self, graph:defaultdict(list)) -> tuple:
        curr_key = 0
        for key in graph.keys():
            curr_key = key
            break
        parity = 0
        value = [0, 0]
        stack = [(curr_key, parity)]
        vis = set([curr_key])
        while stack:
            curr_node, parity = stack.pop()
            value[parity] += 1
            for neg in graph[curr_node]:
                if neg not in vis:
                    vis.add(neg)
                    stack.append((neg, 1 - parity))
        return max(value)


    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        node1 = self.createGraph_ReturnTheNodeWithMostChildren(graph1, edges1)
        node2 = self.createGraph_ReturnTheNodeWithMostChildren(graph2, edges2)

        max_occ = self.countMaxOccOfSubSeq(graph2)

        parity_list = [set(), set()]
        curr_node = 0
        for key in graph1.keys():
            curr_node = key
        stack = [(curr_node, 0)]
        parity_list[0].add(curr_node)
        while stack:
            curr_node, parity = stack.pop()
            for neg in graph1[curr_node]:
                if neg not in parity_list[1 - parity]:
                    parity_list[1 - parity].add(neg)
                    stack.append((neg, 1 - parity))
        res = [0] * (len(edges1) + 1)
        for each_set in parity_list:
            for each_node in each_set:
                res[each_node] += len(each_set) + max_occ


        return res