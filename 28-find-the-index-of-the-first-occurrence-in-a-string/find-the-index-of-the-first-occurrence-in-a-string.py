class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        # Loop through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring of haystack starting at i matches the needle
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1