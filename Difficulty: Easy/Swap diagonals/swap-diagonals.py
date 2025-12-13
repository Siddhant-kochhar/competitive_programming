class Solution:
    def swapDiagonal(self, mat):
      # code here
        n = len(mat)
        for i in range(n):
            # Swapping the elements of major diagonal
            # with minor diagonal
            mat[i][i], mat[i][n - i - 1] = mat[i][n - i - 1], mat[i][i]
        return (mat)