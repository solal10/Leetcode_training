class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j=0,0
        while j<len(abbr) and i<len(word):
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i+=1
                j+=1
            else:
                if abbr[j] == '0':
                    return False
                num=0
                while j<len(abbr) and abbr[j].isdigit():
                    num=num*10+int(abbr[j])
                    j+=1
                i+=num
        return i == len(word) and j == len(abbr)
            