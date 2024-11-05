class Solution:
    def rotate90(self, mat):
        # Rotate the matrix 90 degrees clockwise
        n = len(mat)
        return [[mat[n - j - 1][i] for j in range(n)] for i in range(n)]
    
    def findRotation(self, mat, target):
        for _ in range(4):
            if mat == target:
                return True
            mat = self.rotate90(mat)  # Rotate by 90 degrees
        return False
