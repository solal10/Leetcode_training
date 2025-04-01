class Solution:
    def countVowels(self, word: str) -> int:
        count=0
        vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        for i in range(len(word)):
            if vowels.get(word[i], False):
                count+= (i + 1) * (len(word) - i)
        return count