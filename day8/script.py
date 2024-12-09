import itertools

grid = []

with open('test_input.txt') as file:
    grid = [list(line.strip()) for line in file.readlines()]

locations = {}
for x_index in range(len(grid)):
    for y_index in range(len(grid[0])):
        element = grid[x_index][y_index]
        if element != '.':
            locations[element] = locations.get(
                element, []) + [(x_index, y_index)]


def calculate_antinodes(first, second):
    x_diff = first[0] - second[0]
    y_diff = first[1] - second[1]

    result = []
    first_x = first[0] + x_diff
    first_y = first[1] + y_diff
    if check_outside(first_x) and check_outside(first_y):
        result.append((first_x, first_y))

    second_x = second[0] - x_diff
    second_y = second[1] - y_diff
    if check_outside(second_x) and check_outside(second_y):
        result.append((second_x, second_y))

    return result


def check_outside(coord):
    if coord >= len(grid[0]) or coord < 0:
        return False
    return True


antinodes = set()

for k, v in locations.items():
    for opportunity in itertools.product(v, repeat=2):
        if (opportunity[0] == opportunity[1]):
            continue
        antinodes.update(calculate_antinodes(opportunity[0], opportunity[1]))

for x_index in range(len(grid)):
    line = ""
    for y_index in range(len(grid[0])):
        if (x_index, y_index) in antinodes:
            line += '#'
        else:
            line += grid[x_index][y_index]
    print(line)


print(antinodes)
print(len(antinodes))
