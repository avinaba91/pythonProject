from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        no_of_island = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            else:
                grid[i][j] = 0
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    no_of_island += 1
                    dfs(i, j)
        
        return no_of_island