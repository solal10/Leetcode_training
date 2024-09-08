class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned=set(banned)
        sum_actual=[]
        start=0
        i=1
        while i<=n:
            if i not in banned and sum(sum_actual)+i<=maxSum:
                sum_actual.append(i)
                if sum(sum_actual)==maxSum:
                    break
            elif sum(sum_actual)+i>maxSum:
                break
            i=i+1
        if len(sum_actual) != 0:
            return len(sum_actual)
        else:
            return 0

