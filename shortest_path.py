from collections import deque
def shortest_path(board):
    visited = set()
    queue = deque()
    queue.append((len(board) - 1,0),0)
    shortest_path = int(inf)
    while queue:
        current_place,moves = queue.popleft()
        while current_place != board[0][len(board[0]) - 1] and current_place not in visited:
            moves = [[1,0],[-1,0],[0,1],[0,-1]]
            current_x = current_place[0]
            current_y = current_place[1]
            for x, y in moves:
                if 0 <= current_x + x < len(board) and 0 <= current_y + y < len(board[0]) and board[current_x + x][current_y + y] != 1:
                    queue.append((current_x + x,current_y + y),moves + 1)
        return moves
    return -1
