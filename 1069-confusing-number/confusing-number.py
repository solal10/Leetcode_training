class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation_map = {
        0: 0,
        1: 1,
        6: 9,
        8: 8,
        9: 6}   
        original=n
        rotated_number=0
        while n>0:
            digit= n%10
            if digit not in rotation_map:
                return False
            rotated_number = rotation_map[digit] + rotated_number * 10
            
            n //= 10
        return rotated_number !=original