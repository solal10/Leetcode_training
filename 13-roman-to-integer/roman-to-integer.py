class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='I' and i+1<len(s) :
                if s[i+1]=='V' or s[i+1] =='X':
                    num-=1
                    continue
                else:
                    num+=1
                    continue
            elif s[i]=='I':
                num+=1
                continue
            if s[i] == 'X' and  i+1<len(s):
                if s[i+1]=='L' or s[i+1] =='C':
                    num-=10
                    continue
                else:
                    num+=10
                    continue
            elif s[i] == 'X':
                num+=10
                continue
            if s[i] == 'C' and  i+1<len(s):
                if s[i+1]=='D' or s[i+1] =='M':
                    num-=100
                    continue
                else:
                    num+=100
                    continue
            elif s[i] == 'C':
                num +=100
                continue
            if s[i]=='V':
                num+=5
                continue
            if s[i]=='L':
                num+=50
                continue
            if s[i]=='D':
                num+=500
                continue
            if s[i]=='M':
                num+=1000
                continue
        return num   

            
