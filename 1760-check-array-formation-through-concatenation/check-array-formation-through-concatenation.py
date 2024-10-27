class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index_map = {piece[0]: piece for piece in pieces}
        result = []
        for num in arr:
            if num in index_map:
                result.extend(index_map[num])
        return result == arr
