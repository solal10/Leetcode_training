from collections import Counter

class Solution:
    def makeEqual(self, words):
        # Count total frequency of each character across all strings
        total_count = Counter("".join(words))
        
        # Number of words
        n = len(words)
        
        # Check if each character count is divisible by the number of strings
        for count in total_count.values():
            if count % n != 0:
                return False
        
        return True
