class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='I' and i+1<len(s) :
                if s[i+1]=='V' or s[i+1] =='X':
                    num-=1
                else:
                    num+=1
            elif s[i]=='I':
                num+=1
            if s[i] == 'X' and  i+1<len(s):
                if s[i+1]=='L' or s[i+1] =='C':
                    num-=10
                else:
                    num+=10
            elif s[i] == 'X':
                num+=10
            if s[i] == 'C' and  i+1<len(s):
                if s[i+1]=='D' or s[i+1] =='M':
                    num-=100
                else:
                    num+=100
            elif s[i] == 'C':
                num +=100
            if s[i]=='V':
                num+=5
            if s[i]=='L':
                num+=50
            if s[i]=='D':
                num+=500
            if s[i]=='M':
                num+=1000
        return num   

            
