class Solution:
    def distinctIntegers(self, n: int) -> int:
        board = set([n])
        prev_size = 0
        
        while len(board) != prev_size:
            prev_size = len(board)
            new_nums = set()
            for x in board:
                for i in range(1, n + 1):
                    if x % i == 1:
                        new_nums.add(i)
            board.update(new_nums)
        
        return len(board)       