from typing import List
import functools

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        @functools.lru_cache(None)
        def dp(r_index: int, f_index: int) -> int:
            if r_index == len(robot):
                return 0
            if f_index == len(factory):
                return float('inf')
            
            min_distance = dp(r_index, f_index + 1)
            total_distance = 0
            for k in range(factory[f_index][1]):
                if r_index + k >= len(robot): 
                    break
                total_distance += abs(robot[r_index + k] - factory[f_index][0])
                min_distance = min(min_distance, total_distance + dp(r_index + k + 1, f_index + 1))
            
            return min_distance
        
        return dp(0, 0)
