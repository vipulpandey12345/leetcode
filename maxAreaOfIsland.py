#Nick's solution 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        curVisit = set()
        gMax = 0
       
        def search(r,c):
            if r<0 or r==ROW or c<0 or c==COL or grid[r][c] == 0 or (r,c) in visited:
                return
            visited.add((r,c))
            curVisit.add((r,c))
            search(r+1,c)
            search(r-1,c)
            search(r,c+1)
            search(r,c-1)
       
       
       
       
       
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r,c) not in visited:
                    search(r,c)
                    gMax = max(len(curVisit),gMax)
                    curVisit.clear()
        return gMax
 #Vipul's solution
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])
        if length == 0 or width == 0:
            return 0
        ans = 0
        visited = set()
        for i in range(length):
            for j in range(width):
                current = 0
                if grid[i][j] == 1 and (i,j) not in visited:
                    helper(length, width, grid, i, j, visited, ans, current)
        return ans 
    def helper(length, width, grid, i, j, visited, ans, current):
        if (i,j) in visited:
            ans = max(ans, current)
            return
        current += 1
        visited.add((i,j))
        for x1, y1 in [(0,1),(1,0),(-1,0),(0,-1)]:
            new_x, new_y = i + x1, j + y1
            if 0 <= new_x < length and 0 <= new_y < height:
                new_position = grid[new_x][new_y]
                if new_position == 1:
                    helper(length, width, grid, new_x, new_y, visited, ans, current)


      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
