class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        flag=False
        for i in range(left,right+1):
            for inter in ranges:
                if i >= inter[0] and i<= inter[1]:
                    flag=True
                    break
            if flag==False:
                return False
            else:
                flag=False
        return True    