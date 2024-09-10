import re
def remove_non_alphanumeric(input_string):
    # Use regex to replace all non-alphanumeric characters with an empty string
    return re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=remove_non_alphanumeric(s)
        j=len(newstr)-1
        i=0
        while(i<j):
            if newstr[i] !=newstr[j]:
                return False
            i+=1
            j-=1
        return True

        