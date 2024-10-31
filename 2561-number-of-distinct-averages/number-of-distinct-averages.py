
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        distinct_averages = set()
        
        while nums:
            min_num = min(nums)
            max_num = max(nums)
            nums.remove(min_num)
            nums.remove(max_num)
            average = (min_num + max_num) / 2
            distinct_averages.add(average)
        
        return len(distinct_averages)
