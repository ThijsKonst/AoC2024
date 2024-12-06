grid = []

with open('input.txt') as file:
    grid = [[char for char in line.strip()] for line in file.readlines()]

print(grid)
dir_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]

x_pos = next(grid.index(x) for x in grid if '^' in x)
y_pos = grid[x_pos].index('^')
dir = 0
visited = set([(x_pos, y_pos)])


def move(x, y, dir):
    new_x = x + dir_list[dir][0]
    new_y = y + dir_list[dir][1]
    if x == -1 or y == -1 or new_x == len(grid) or new_y == len(grid):
        return -1, -1, 0

    if grid[new_x][new_y] == '#':
        return x, y, (dir + 1) % 4
    return new_x, new_y, dir


while True:
    x_pos, y_pos, dir = move(x_pos, y_pos, dir)
    if x_pos == -1:
        break
    visited.add((x_pos, y_pos))


print(len(visited))
