# https://leetcode.com/problems/number-of-islands/

class Solution:
    def __init__(self):
        self.grid = None

    def get_neighbors(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])

        valid_neighbors = []

        shifts = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        for shift in shifts:
            if 0 <= (i + shift[0]) < n and 0 <= (j + shift[1]) < m:
                valid_neighbors.append([i + shift[0], j + shift[1]])

        return valid_neighbors

    def colonize(self, i, j):
        self.grid[i][j] = 'X'

        valid_neighbors = self.get_neighbors(self.grid, i, j)

        for i, j in valid_neighbors:
            if self.grid[i][j] == '1':
                self.colonize(i, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if not self.grid:
            self.grid = grid

        number_of_components = 0

        for i in range(n):
            for j in range(m):
                if self.grid[i][j] == '1':
                    self.colonize(i, j)
                    number_of_components += 1

        return number_of_components







