class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        surface_area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    surface_area += grid[i][j] * 6
                    surface_area -= (grid[i][j] - 1) * 2
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= x < n and 0 <= y < n:
                            surface_area -= min(grid[i][j], grid[x][y])
        return surface_area
