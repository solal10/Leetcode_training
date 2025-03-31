from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = n * 3
        # Create a fine-grained grid, each cell is 3x3
        graph = [[0] * size for _ in range(size)]

        for i in range(n):
            for j in range(n):
                char = grid[i][j]
                r, c = i * 3, j * 3
                if char == '/':
                    graph[r][c+2] = 1
                    graph[r+1][c+1] = 1
                    graph[r+2][c] = 1
                elif char == '\\':
                    graph[r][c] = 1
                    graph[r+1][c+1] = 1
                    graph[r+2][c+2] = 1

        def dfs(x, y):
            if x < 0 or x >= size or y < 0 or y >= size or graph[x][y] == 1:
                return
            graph[x][y] = 1
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(x+dx, y+dy)

        regions = 0
        for i in range(size):
            for j in range(size):
                if graph[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions
