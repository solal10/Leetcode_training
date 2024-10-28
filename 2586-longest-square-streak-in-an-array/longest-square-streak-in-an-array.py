class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = -1

        for num in num_set:
            length = 0
            current = num
            while current in num_set:
                length += 1
                current *= current
            if length >= 2:
                max_length = max(max_length, length)

        return max_length
