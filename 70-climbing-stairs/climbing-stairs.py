class Solution:
    def climbStairs(self, n: int) -> int:
        x1=0
        x2=1
        total_sum=0
        for i in range(n):
            total_sum=x1+x2
            x1=x2
            x2=total_sum
        return total_sum
