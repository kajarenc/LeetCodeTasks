# https://leetcode.com/problems/max-area-of-island/submissions/
from typing import List
# https://leetcode.com/problems/max-area-of-island/submissions/


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = [[0] * m for _ in range(n)]

        max_area = 0
        area = 0

        def dfs(i, j):
            nonlocal area
            nonlocal visited

            area += 1
            visited[i][j] = 1

            for dx, dy in neighbors:
                if 0 <= i + dx < n and 0 <= j + dy < m and grid[i + dx][j + dy] and not visited[i + dx][j + dy]:
                    dfs(i + dx, j + dy)

        for x in range(n):
            for y in range(m):
                if grid[x][y] and not visited[x][y]:
                    area = 0
                    dfs(x, y)

                    if area > max_area:
                        max_area = area

        return max_area
