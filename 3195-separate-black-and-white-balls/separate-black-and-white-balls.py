class Solution:
    def minimumSteps(self, s: str) -> int:
        black_positions = [i for i, ball in enumerate(s) if ball == '1']
        num_black = len(black_positions)
        swaps = 0
        for i, current_position in enumerate(black_positions):
            target_position = len(s) - num_black + i
            swaps += abs(target_position - current_position)
        return swaps