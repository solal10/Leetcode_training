class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        count=0
        new_word=word
        while True:
            if new_word in sequence:
                new_word=new_word+word
                count+=1
            else:
                return count