class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        shift_n=n>>1
        xor_n=n^shift_n
        return (xor_n & (xor_n+1)==0)