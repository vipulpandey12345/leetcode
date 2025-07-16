class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if (i,j) in visited:
                return
            if grid[i][j] == '0':
                return
            visited.add((i,j))
            moves = [[1,0],[-1,0],[0,1],[0,-1]]
            for x, y in moves:
                if 0 <= x + i < length:
                    if 0 <= y + j < width:
                        dfs(x + i, y + j)
        length = len(grid)
        width = len(grid[0])
        visited = set()
        number_of_islands = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == '1' and (i,j) not in visited:
                    number_of_islands += 1
                    dfs(i,j)
        return number_of_islands
        
