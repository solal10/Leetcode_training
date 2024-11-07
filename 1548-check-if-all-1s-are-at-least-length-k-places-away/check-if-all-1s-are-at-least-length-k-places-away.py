class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count =k
        for i in range(len(nums)):
            if nums[i]==1:
                if count>=k:
                    count=0
                else:
                    return False
            else:
                count+=1
        return True