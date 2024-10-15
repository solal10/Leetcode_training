class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        Pop_by_year={}
        for i in logs:
            if i[0] in Pop_by_year:
                Pop_by_year[i[0]]+=1
            else:
                Pop_by_year[i[0]]=1
            if i[1] in Pop_by_year:
                Pop_by_year[i[1]]-=1
            else:
                 Pop_by_year[i[1]]=-1

        sorted_pop = dict(sorted(Pop_by_year.items()))
        popu=0
        max_popu=0
        year=next(iter(sorted_pop.keys()))
        for key in sorted_pop:
            popu+=sorted_pop[key]
            if max_popu<popu:
                max_popu=popu
                year=key
        return year

                