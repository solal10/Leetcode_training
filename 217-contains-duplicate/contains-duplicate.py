class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_value=set()
        for num in nums:
            if num in seen_value:
                return True
            else:
                seen_value.add(num)
        return False