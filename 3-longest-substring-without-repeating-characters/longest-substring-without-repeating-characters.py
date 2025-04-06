class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index={}
        start=0
        max_length=0

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start=char_index[s[end]]+1
            else:
                max_length=max(max_length,end-start+1)
            char_index[s[end]]=end
        return max_length
