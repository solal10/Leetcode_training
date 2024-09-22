class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count_max=0
        index_max=0
        for i in range(len(mat)):
            if sum(mat[i])>count_max:
                count_max=sum(mat[i])
                index_max=i
        return [index_max,count_max]
