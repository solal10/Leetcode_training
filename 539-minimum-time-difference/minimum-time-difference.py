class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(time: str) -> int:
            h, m = map(int, time.split(":"))
            return h * 60 + m

        minutes=[convert_to_minutes(time) for time in timePoints]
        minutes.sort()
        current_min=float('inf')
        for i in range(1, len(minutes)):
            current_min = min(current_min, minutes[i] - minutes[i - 1])
        circular_diff = 1440 + minutes[0] - minutes[-1]
        current_min = min(current_min, circular_diff)
        return current_min