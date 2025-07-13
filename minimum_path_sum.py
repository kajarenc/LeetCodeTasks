# https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        min_matrix = [[0] * m for _ in range(n)]
        min_matrix[0][0] = grid[0][0]

        for i in range(1, n):
            min_matrix[i][0] = min_matrix[i - 1][0] + grid[i][0]

        for j in range(1, m):
            min_matrix[0][j] = min_matrix[0][j - 1] + grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                min_matrix[i][j] = (
                    min(min_matrix[i - 1][j], min_matrix[i][j - 1]) + grid[i][j]
                )

        return min_matrix[n - 1][m - 1]
