class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        low=0
        high=n-1
        while low<=high:
            mid = (low + high) // 2
            if citations[mid]>=n-mid:
                high=mid-1
            else:
                low=mid+1
        return n-low