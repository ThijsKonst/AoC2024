grid = []

with open('test_input.txt') as file:
    grid = [list(line.strip()) for line in file.readlines()]

dir_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]
x_start = next(grid.index(x) for x in grid if '^' in x)
y_start = grid[x_start].index('^')
dir = 0
visited = set()


def move(x, y, dir, obstacle):
    new_x = x + dir_list[dir][0]
    new_y = y + dir_list[dir][1]
    if x == -1 or y == -1 or new_x == len(grid) or new_y == len(grid):
        return -1, -1, 0

    if grid[new_x][new_y] == '#' or (new_x, new_y) == obstacle:
        return x, y, (dir + 1) % 4
    return new_x, new_y, dir


x_pos = x_start
y_pos = y_start
while True:
    x_pos, y_pos, dir = move(x_pos, y_pos, dir, (-1, -1))
    if x_pos == -1:
        break
    visited.add((x_pos, y_pos))


loops = 0
for obstacle in visited:
    x_pos = x_start
    y_pos = y_start
    if obstacle == (x_pos, y_pos):
        continue
    dir = 0
    visited_dir = set([(x_pos, y_pos, dir)])

    while True:
        x_pos, y_pos, dir = move(x_pos, y_pos, dir, obstacle)
        if x_pos == -1:
            break
        if (x_pos, y_pos, dir) in visited_dir:
            loops += 1
            break
        visited_dir.add((x_pos, y_pos, dir))

print(loops)
