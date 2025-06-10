class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        number_of_servers = 0
        length_of_grid = len(grid)
        width_of_grid = len(grid[0])
        visited = set()

        increment_for_width = 0
        increment_for_length = 0

        while increment_for_width < width_of_grid:
            row, col = increment_for_length, increment_for_width

            # Check column
            servers_in_col = [i for i in range(length_of_grid) if grid[i][col] == 1]
            if len(servers_in_col) > 1:
                for i in servers_in_col:
                    if (i, col) not in visited:
                        visited.add((i, col))
                        number_of_servers += 1

            # Check row
            servers_in_row = [j for j in range(width_of_grid) if grid[row][j] == 1]
            if len(servers_in_row) > 1:
                for j in servers_in_row:
                    if (row, j) not in visited:
                        visited.add((row, j))
                        number_of_servers += 1

            if increment_for_length + 1 != length_of_grid:
                increment_for_length += 1
            increment_for_width += 1

        return number_of_servers
