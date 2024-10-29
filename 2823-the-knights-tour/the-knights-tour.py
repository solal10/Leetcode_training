class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = [[-1 for _ in range(n)] for _ in range(m)]
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and board[x][y] == -1

        def count_onward_moves(x, y):
            count = 0
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    count += 1
            return count

        def backtrack(x, y, step):
            board[x][y] = step
            if step == m * n - 1:
                return True
            next_moves = []
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    next_moves.append((count_onward_moves(nx, ny), nx, ny))
            next_moves.sort()  # Sort by least onward moves first

            for _, nx, ny in next_moves:
                if backtrack(nx, ny, step + 1):
                    return True
            board[x][y] = -1  # Backtrack
            return False

        backtrack(r, c, 0)
        return board
