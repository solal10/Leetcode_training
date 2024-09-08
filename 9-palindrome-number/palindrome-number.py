class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_pal=str(x)
        for i in range(len(num_pal)//2):
            if num_pal[i]!=num_pal[len(num_pal) - i - 1]:
                return False
        return True
