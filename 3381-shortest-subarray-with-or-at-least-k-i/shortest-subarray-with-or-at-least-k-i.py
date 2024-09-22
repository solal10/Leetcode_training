class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def bitwise_or_of_subarray(subarray):
            result = 0
            for num in subarray:
                result |= num
            return result
        
        subarrays = []
        for start in range(len(nums)):
            subarray = []
            for end in range(start, len(nums)):
                subarray.append(nums[end])
                subarrays.append(subarray[:])
        length_sub=float('inf')
        for subarray in subarrays:
            if len(subarray)<length_sub and bitwise_or_of_subarray(subarray)>=k:
                length_sub=len(subarray)
        if length_sub==float('inf'):
            return -1
        return length_sub
                