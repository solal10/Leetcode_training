import heapq


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        heap = []  # Max heap: stores (-yi + xi, xi)

        for xj, yj in points:
            # Remove points that are too far (xj - xi > k)
            while heap and xj - heap[0][1] > k:
                heapq.heappop(heap)

            # If the heap isn't empty, compute the value using the top element
            if heap:
                max_value = max(max_value, -heap[0][0] + yj + xj)

            # Push the current point as a candidate for future pairs
            # We push -yi + xi to simulate max heap
            heapq.heappush(heap, (-(yj - xj), xj))

        return max_value