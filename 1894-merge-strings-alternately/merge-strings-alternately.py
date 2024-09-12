class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newword = ""
        count = 0
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(word1) and pointer2 < len(word2):
            if count == 0:
                newword += word1[pointer1]
                pointer1 += 1
                count = 1
            else:
                newword += word2[pointer2]
                pointer2 += 1
                count = 0
        while pointer1 < len(word1):
            newword += word1[pointer1]
            pointer1 += 1
        while pointer2 < len(word2):
            newword += word2[pointer2]
            pointer2 += 1
        return newword

            

