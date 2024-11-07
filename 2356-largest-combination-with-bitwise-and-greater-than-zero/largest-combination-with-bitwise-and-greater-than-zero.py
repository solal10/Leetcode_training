class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
            
        max_count = 0
        # We check 24 bits (enough for common positive integers)
        for bit in range(24):  
            count = 0
            for num in candidates:
                # Check if the 'bit'-th bit is 1 for this number
                if (num >> bit) & 1:
                    count += 1
            max_count = max(max_count, count)  # Keep track of the highest count
        return max_count