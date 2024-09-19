class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sorted_array=[]
        for num in nums:
            if num % 2 ==0 :
                sorted_array.insert(0,num)
            else:
                sorted_array.append(num)
        return sorted_array