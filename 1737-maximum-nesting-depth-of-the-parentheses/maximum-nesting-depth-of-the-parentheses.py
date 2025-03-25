class Solution:
    def maxDepth(self, s: str) -> int:
        max_count=0
        count=0
        for c in s:
            if c =='(':
                count+=1
            if c ==')':
                max_count=max(max_count,count)
                count-=1
        return max_count