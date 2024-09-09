class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        indexstart = -1
        indexneedle = 0
        i=0
        while i < len(haystack):            
            if haystack[i] == needle[indexneedle]:
                if indexstart == -1:
                    indexstart = i
                indexneedle += 1
            else:
                if indexstart != -1:
                    i = indexstart  
                indexstart = -1
                indexneedle = 0

            if indexneedle == len(needle):
                return indexstart
            i+=1
        return -1
