class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_length = 0
        count0, count1 = 0, 0

        i = 0
        while i < len(s):
            count0, count1 = 0, 0
            
            while i < len(s) and s[i] == '0':
                count0 += 1
                i += 1
            
            while i < len(s) and s[i] == '1':
                count1 += 1
                i += 1
            
            max_length = max(max_length, 2 * min(count0, count1))
        
        return max_length
