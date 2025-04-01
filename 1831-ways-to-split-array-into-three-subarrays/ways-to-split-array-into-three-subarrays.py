from bisect import bisect_left, bisect_right

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        res = 0

        for i in range(1, n - 1):
            left_sum = prefix[i]

            j_left = bisect_left(prefix, 2 * left_sum, i + 1, n)

            j_right = bisect_right(prefix, (prefix[n] + prefix[i]) // 2, i + 1, n)

            if j_left <= j_right:
                res = (res + (j_right - j_left)) % MOD

        return res
