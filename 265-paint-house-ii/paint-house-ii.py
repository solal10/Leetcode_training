class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])

        # Initialize the first row's minimums
        min1, min2 = -1, -1

        for j in range(k):
            if min1 == -1 or costs[0][j] < costs[0][min1]:
                min2 = min1
                min1 = j
            elif min2 == -1 or costs[0][j] < costs[0][min2]:
                min2 = j

        # Process each house starting from the second one
        for i in range(1, n):
            new_min1, new_min2 = -1, -1
            for j in range(k):
                if j == min1:
                    costs[i][j] += costs[i - 1][min2] if min2 != -1 else 0
                else:
                    costs[i][j] += costs[i - 1][min1] if min1 != -1 else 0

                # Update new_min1 and new_min2 for the current row
                if new_min1 == -1 or costs[i][j] < costs[i][new_min1]:
                    new_min2 = new_min1
                    new_min1 = j
                elif new_min2 == -1 or costs[i][j] < costs[i][new_min2]:
                    new_min2 = j

            min1, min2 = new_min1, new_min2

        return costs[-1][min1] if min1 != -1 else 0
