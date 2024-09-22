class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Helper function to count steps between prefix and the next prefix
        def count_steps(prefix: int, n: int) -> int:
            current = prefix
            next_prefix = prefix + 1
            steps = 0
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps

        curr = 1
        k -= 1  # Because we're starting from the first number

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                # Move to the next prefix
                curr += 1
                k -= steps
            else:
                # Go deeper in the current prefix tree
                curr *= 10
                k -= 1

        return curr
