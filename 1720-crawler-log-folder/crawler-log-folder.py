from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                # Move up a folder, but don't go above the main folder
                if depth > 0:
                    depth -= 1
            elif log != "./":
                # Move to a child folder
                depth += 1
        return depth
