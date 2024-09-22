class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count_boundary=0
        position_of_ant=0
        for num in nums:

            position_of_ant+=num
            if position_of_ant == 0:
                count_boundary+=1
        return count_boundary