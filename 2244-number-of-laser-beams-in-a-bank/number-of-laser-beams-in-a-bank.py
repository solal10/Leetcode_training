class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_devices = 0
        count = 0

        for row in bank:
            curr_devices = row.count('1')
            if curr_devices == 0:
                continue
            count += prev_devices * curr_devices
            prev_devices = curr_devices
        return count