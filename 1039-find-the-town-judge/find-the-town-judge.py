class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree=[0]*n
        outdegree=[0]*n
        for relation in trust:
            outdegree[relation[0]-1]+=1
            indegree[relation[1]-1]+=1
        for i in range(n):
            if indegree[i]==n-1 and outdegree[i]==0:
                return i+1
        return -1
