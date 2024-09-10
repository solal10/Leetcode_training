class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0):
            return 0
        i=1
        while True:
            if i*i == x :
                return i
            if (i-1)*(i-1)<x and (i+1)*(i+1)>x:
                return i
            i+=1