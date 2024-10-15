import math

class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            for j in range(1,n+1,1):
                c_squared=(i*i) +(j*j)
                c = math.isqrt(c_squared)
                if c*c==c_squared and c<=n:
                    count+=1
        return count