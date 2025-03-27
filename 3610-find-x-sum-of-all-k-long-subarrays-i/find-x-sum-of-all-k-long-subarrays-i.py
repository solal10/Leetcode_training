from collections import Counter
import heapq
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def get_x_sum(subarr: List[int], x: int) -> int:
            freq = Counter(subarr)
            heap = [(-count, -num) for num, count in freq.items()]
            heapq.heapify(heap)

            top_x = set()
            for _ in range(min(x, len(heap))):
                _, num = heapq.heappop(heap)
                top_x.add(-num)
            
            return sum(num for num in subarr if num in top_x)

        n = len(nums)
        result = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            result.append(get_x_sum(subarray, x))

        return result
