class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            max_move = 0
            for dr in [-1, 0, 1]:  # directions: up-right, right, down-right
                new_row, new_col = row + dr, col + 1
                if 0 <= new_row < m and new_col < n and grid[new_row][new_col] > grid[row][col]:
                    max_move = max(max_move, 1 + dfs(new_row, new_col))
            memo[(row, col)] = max_move
            return max_move

        result = 0
        for i in range(m):
            result = max(result, dfs(i, 0))
        return result
