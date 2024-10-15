class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        count = 0
        for l, w in rectangles:
            side = min(l, w)
            if side > maxLen:
                maxLen = side
                count = 1
            elif side == maxLen:
                count += 1
        return count