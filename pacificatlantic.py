'''
- DFS seeing if you can reach (leftmost column or upper most row) & (rightmost column or lowermost row)
- keep track of visited squares
'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,visited_set):
            if (i,j) in visited_set:
                return
            visited_set.add((i,j))
            moves = [[1,0],[-1,0],[0,1],[0,-1]]
            for x, y in moves:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < len(heights) and 0 <= new_j < len(heights[0]):
                    if heights[i][j] <= heights[new_i][new_j] and (new_i, new_j) not in visited_set:
                        dfs(new_i, new_j, visited_set)

        pacific_visited = set()
        atlantic_visited = set()
        res = []
        #process all cells on pacific side
        for row in range(len(heights)):
            dfs(row,0,pacific_visited)
        for col in range(len(heights[0])):
            dfs(0,col,pacific_visited)
        #process all cells on atlantic side
        for row in range(len(heights)):
            dfs(row,len(heights[0]) - 1,atlantic_visited)
        for col in range(len(heights[0])):
            dfs(len(heights) - 1, col, atlantic_visited)
        for entry in pacific_visited:
            if entry in atlantic_visited:
                res.append([entry[0],entry[1]])
        return res
        
