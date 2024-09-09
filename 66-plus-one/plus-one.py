class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        digits[-1] += 1
        carry = 0
        
        if digits[-1] == 10:
            digits[-1] = 0
            carry = 1
        else:
            return digits
        
        for i in range(n - 2, -1, -1):
            if carry:
                digits[i] += 1
                if digits[i] == 10:
                    digits[i] = 0
                    carry = 1  
                else:
                    carry = 0  
                    break 
            else:
                break  
        
        if carry:
            digits.insert(0, 1)
        
        return digits