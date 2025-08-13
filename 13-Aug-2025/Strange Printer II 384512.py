# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def in_compass(self, corr, parent_color, child_color, target_grid) -> bool:

        parent_top, parent_left  = corr[parent_color][0], corr[parent_color][1]
        parent_bottom, parent_right = corr[parent_color][2], corr[parent_color][3]

        child_top, child_left  = corr[child_color][0], corr[child_color][1]
        child_bottom, child_right = corr[child_color][2], corr[child_color][3]

        for row in range(parent_top, parent_bottom + 1):
            for col in range(parent_left, parent_right + 1):
                if target_grid[row][col] == child_color:
                    return True
        return False


        

    def build_matrix(self, coordinate, color, matrix):
        top = coordinate[0]
        left = coordinate[1]
        bottom = coordinate[2]
        right = coordinate[3]
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                matrix[row][col] = color

    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        node_scope_map = defaultdict(Counter)
        len_row, len_col = len(targetGrid), len(targetGrid[0])
        in_bound = lambda x, y: 0 <= x < len_row and 0 <= y < len_col
        for row in range(len(targetGrid)):
            for col in range(len(targetGrid[0])):
                if targetGrid[row][col] != 0:
                    val = targetGrid[row][col]
                    if val in node_scope_map:
                        node_scope_map[val][0] = min(node_scope_map[val][0], row)
                        node_scope_map[val][1] = min(node_scope_map[val][1], col)
                        node_scope_map[val][2] = max(node_scope_map[val][2], row)
                        node_scope_map[val][3] = max(node_scope_map[val][3], col)
                    else:
                        node_scope_map[val] = [row, col, row, col]
        
        topological_graph = defaultdict(list)
        in_degree = Counter()
        for color_parent, parent_corner_coordinate in node_scope_map.items():
            for color_child, child_corner_coordinate in node_scope_map.items():
                if color_parent != color_child and self.in_compass(node_scope_map, color_parent, color_child, targetGrid):
                    topological_graph[color_parent].append(color_child)
                    in_degree[color_child] += 1
        
        matrix = [[0] * len(targetGrid[0]) for _ in range(len(targetGrid))]
        order = deque()
        for color in node_scope_map.keys():
            if in_degree[color] == 0:
                order.append(color)
       
        while order:
            curr_color = order.popleft()
            
            self.build_matrix(node_scope_map[curr_color], curr_color, matrix)
            for child_color in topological_graph[curr_color]:
                in_degree[child_color] -= 1
                if in_degree[child_color] == 0:
                    order.append(child_color)
        
        return matrix == targetGrid