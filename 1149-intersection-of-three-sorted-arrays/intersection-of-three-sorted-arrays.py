class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result1=set()
        for i in range(len(arr1)):
            if arr1[i] in arr2 and arr1[i] in arr3 and arr1[i] not in result1:
                result1.add(arr1[i])
        return sorted(list(result1))