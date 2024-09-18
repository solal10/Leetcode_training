class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        for i in range(len(columnTitle)):
            value = ord(columnTitle[i]) - ord('A') + 1
            result+= (value*(26**(len(columnTitle) - i - 1)))
        return result
