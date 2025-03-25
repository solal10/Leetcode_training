class Solution:
    def canAliceWin(self, n: int) -> bool:
        move=10
        turn=0
        while n >= move:
            n -= move
            move -= 1
            turn ^= 1
        return turn == 1