class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_array = list(magazine)
        for c in ransomNote:
            if c in mag_array:
                mag_array.remove(c)
            else:
                return False
        return True