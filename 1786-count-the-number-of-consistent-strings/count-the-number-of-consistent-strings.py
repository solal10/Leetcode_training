class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        flag=0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    flag=1
                    break
            if flag != 1:
                count+=1
            flag=0
        return count