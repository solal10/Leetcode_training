import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        log_four=math.log(n,4)
        return log_four.is_integer()
        