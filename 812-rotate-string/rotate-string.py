class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        newS=s+s
        if goal in newS:
            return True
        return False