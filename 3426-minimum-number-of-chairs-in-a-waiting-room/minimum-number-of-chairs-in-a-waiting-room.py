class Solution:
    def minimumChairs(self, s: str) -> int:
        max_chair_needed=0
        current_chair=0
        for act in s:
            if act =='E':
                current_chair+=1
                if current_chair>max_chair_needed:
                    max_chair_needed=current_chair
            if act =='L':
                current_chair-=1
        return max_chair_needed
