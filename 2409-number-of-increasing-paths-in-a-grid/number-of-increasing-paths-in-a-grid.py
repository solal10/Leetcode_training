from typing import List
from functools import lru_cache

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        @lru_cache(None)
        def dfs(i, j):
            res = 1  # The path that starts and ends at (i, j)
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    res += dfs(ni, nj)
                    res %= MOD
            return res

        total = 0
        for i in range(m):
            for j in range(n):
                total += dfs(i, j)
                total %= MOD

        return total
