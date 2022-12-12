# a-z,  S current pos, E destination
# S a, E z

import heapq

def dijkstra(grid, start, destination):
    rows = len(grid)
    cols = len(grid[0])
    
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    
    pq = [(0, start)]
    prev = {}
    
    while pq:
        dist, curr = heapq.heappop(pq)
        
        if curr == destination:
            break
        
        for neighbor in get_neighbors(curr, grid):
            row, col = neighbor
            if grid[curr[0]][curr[1]] < (grid[row][col] - 1):
                continue
            new_dist = dist + 1
            if new_dist < distances[row][col]:
                distances[row][col] = new_dist
                prev[neighbor] = curr
                heapq.heappush(pq, (new_dist, neighbor))
    
    if destination not in prev:
        return None
    
    # path = []
    curr = destination
    steps = 0
    while curr != start:
        steps += 1
        # path.append(curr)
        curr = prev[curr]
    
    # path.append(start)
    # path.reverse()
    # print('Paht: ', path)
    
    return steps

def get_neighbors(node, grid):
    row, col = node
    rows = len(grid)
    cols = len(grid[0])
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    
    for offset in offsets:
        new_row = row + offset[0]
        new_col = col + offset[1]
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col))
    
    return neighbors

def process_grid(input_file):
    grid = []
    start_attempts = []
    for line in open(input_file).readlines():
        grid.append([])
        for node in line[:-1]:
            height = ord(node)
            coords = (len(grid)-1, len(grid[len(grid)-1]))
            if node == 'S':
                start = coords
                height = ord('a')
            if node == 'E':
                end = coords
                height = ord('z')
            if node == 'a':
                start_attempts.append(coords)
            grid[len(grid)-1].append(height)
    return (grid, start, start_attempts, end)

if __name__ == '__main__':
    grid, start, start_attempts, dest = process_grid('12/input')
    print('01: ', dijkstra(grid, start, dest))
    
    attempts = []
    for start in start_attempts:
        steps = dijkstra(grid, start, dest)
        if steps: attempts.append(steps)
    
    print('02: ', min(attempts))
