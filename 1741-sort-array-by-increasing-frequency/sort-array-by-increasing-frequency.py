
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency_dict = {}
        for value in nums:
            if value in frequency_dict:
                frequency_dict[value] += 1
            else:
                frequency_dict[value] = 1
        sorted_dict = dict(sorted(frequency_dict.items(), key=lambda item: (item[1], -item[0])))
        result = []
        for value, frequency in sorted_dict.items():
            result.extend([value] * frequency)

        return result
