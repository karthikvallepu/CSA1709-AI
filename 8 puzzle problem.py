from collections import deque

goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]   

moves = [(1,0), (-1,0), (0,1), (0,-1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def bfs(start):
    visited = set()
    q = deque([(start, [])])
    while q:
        state, path = q.popleft()
        if state == goal_state:
            return path + [state]
        state_tuple = tuple(map(tuple, state))
        if state_tuple not in visited:
            visited.add(state_tuple)
            for neighbor in get_neighbors(state):
                q.append((neighbor, path + [state]))
    return None

start_state = [[1,2,3],
               [4,0,6],
               [7,5,8]]

solution = bfs(start_state)

if solution:
    print("Steps to solve the puzzle:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
