class Solution:
    def findLatestTime(self, s: str) -> str:
        h1, h2, colon, m1, m2 = s

        if h1 == '?':
            if h2 == '?' or '0' <= h2 <= '1':
                h1 = '1'
            else:
                h1 = '0'
        if h2 == '?':
            if h1 == '1':
                h2 = '1'
            else:
                h2 = '9'
        if m1 == '?':
            m1 = '5'
        if m2 == '?':
            m2 = '9'
        return f"{h1}{h2}:{m1}{m2}"
