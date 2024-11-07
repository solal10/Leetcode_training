from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        max_pos = arr.index(max(arr))
        if max_pos == 0 or max_pos == len(arr) - 1:
            return False
        for i in range(0, max_pos):
            if arr[i] >= arr[i + 1]:
                return False
        for i in range(max_pos, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True
