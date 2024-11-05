class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double=0
        for num in nums:
            if 0 <= num <= 9:  # Check if the number is a single-digit
                single += num
            else:
                double+=num
        return single !=double
