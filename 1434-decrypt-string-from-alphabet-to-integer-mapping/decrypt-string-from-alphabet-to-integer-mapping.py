class Solution:
    def freqAlphabets(self, s: str) -> str:
        new_s=''
        i=0
        while i <len(s):
            if i+2 < len(s) and s[i+2] == '#':
                 new_s += chr(int(s[i:i+2]) + 96)
                 i+=3
            else:
                new_s += chr(int(s[i]) + 96)
                i+=1
        return new_s