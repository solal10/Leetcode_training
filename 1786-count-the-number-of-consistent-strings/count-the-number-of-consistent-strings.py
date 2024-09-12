class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count=0
        for word in words:
            if all(letter in allowed_set for letter in word):
                count += 1
        return count