class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special_count = 0

        for ch in range(26):
            lower = chr(ord('a') + ch)
            upper = chr(ord('A') + ch)

            if lower in word and upper in word:
                first_upper_index = word.index(upper)
                # Check if all lowercase letters are before the first uppercase
                if all(i < first_upper_index for i, c in enumerate(word) if c == lower):
                    special_count += 1

        return special_count
