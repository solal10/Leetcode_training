from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
    # First, count the number of zeros to be duplicated
        zeros = arr.count(0)
        n = len(arr)

    # We will iterate backwards, starting from the last element that will stay within bounds
        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]

            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0