class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)  # Convert string to list for easy modification
        
        # Iterate through each character in the string
        for i in range(len(s)):
            if s[i] == '?':
                # Check adjacent characters to avoid repeating
                for char in 'abc':  # We use 'a', 'b', 'c' because any solution will work
                    # Check the previous and next characters
                    if (i > 0 and s[i - 1] == char) or (i < len(s) - 1 and s[i + 1] == char):
                        continue
                    s[i] = char  # Replace '?' with valid character
                    break
        
        return ''.join(s)  # Convert list back to string