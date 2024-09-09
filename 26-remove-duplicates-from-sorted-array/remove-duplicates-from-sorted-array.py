class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i =0
        inList=[]
        while i<len(nums):
            if nums[i] in inList:
                nums.pop(i)
            else:
                inList.append(nums[i])
                i+=1
        return len(nums)