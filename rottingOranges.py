#edit this solution
 def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        queue = deque()
        answer = 0
        visited = set()
        length = len(grid)
        width = len(grid[0])
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 2:
                    position = (i,j)
                    queue.append(position)
        if len(queue) == 0:
            return -1
        #start BFS at positions in the queue
        while queue:
            answer += 1
            i = len(queue)
            while i:
                positions = [(0,1), (0,-1), (1,0), (-1,0)]
                x, y  = queue.popleft()
                for new_x,new_y in positions:
                    if (x + new_x, y + new_y) in visited:
                        continue
                    if 0 <= x + new_x <= length - 1 and  0 <= y + new_y <= width - 1:
                        if grid[x + new_x][y + new_y] == 1:
                            grid[x + new_x][y + new_y] == 2
                            visited.add((x + new_x, y + new_y))
                            queue.append((x + new_x, y + new_y))
                i -= 1
        return answer - 1
                        
