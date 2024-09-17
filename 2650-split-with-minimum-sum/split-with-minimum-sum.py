class Solution:
    def splitNum(self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        digits.sort()
        num1=0
        num2=0
        for i in range(len(digits)):
            if i%2==0:
               num1= num1*10 + digits[i]
            else:
                num2=num2*10 +digits[i]
        return num1 + num2 

