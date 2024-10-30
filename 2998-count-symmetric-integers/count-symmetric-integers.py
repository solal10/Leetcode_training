from typing import List

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(x: int) -> bool:
            s = str(x)
            if len(s) % 2 != 0:
                return False
            n = len(s) // 2
            first_half = s[:n]
            second_half = s[n:]
            return sum(map(int, first_half)) == sum(map(int, second_half))

        count = 0
        for x in range(low, high + 1):
            if is_symmetric(x):
                count += 1
        return count
