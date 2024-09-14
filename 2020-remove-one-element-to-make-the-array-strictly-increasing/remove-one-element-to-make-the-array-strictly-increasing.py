class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            temparray = nums[:i] + nums[i+1:]
            flagin=True
            for j in range(1,n-1):
                if temparray[j]<=temparray[j-1]:
                    flagin=False
                    break
            if flagin:
                return True
        return False