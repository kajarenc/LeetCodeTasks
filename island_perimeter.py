from typing import List


# "brute force" approach
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        p = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:

                    for dx, dy in neighbors:
                        if 0 <= i + dx < n and 0 <= j + dy < m:
                            if grid[i + dx][j + dy] == 0:
                                p += 1
                        else:
                            p += 1
        return p


# DFS approach
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        land_i = -1
        land_j = -1
        land_found = False

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    land_i = i
                    land_j = j
                    land_found = True
                    break
            if land_found:
                break

        p = 0
        visited = set()

        def dfs(i, j):
            nonlocal p
            if (i, j) not in visited:
                visited.add((i, j))

                for dx, dy in neighbors:
                    if 0 <= i + dx < n and 0 <= j + dy < m:
                        if grid[i + dx][j + dy] == 0:
                            p += 1
                        else:
                            dfs(i + dx, j + dy)
                    else:
                        p += 1

        dfs(land_i, land_j)
        return p
