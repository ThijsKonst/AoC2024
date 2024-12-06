chars = []

with open('input.txt') as file:
    for line in file:
        carlines = []
        for char in line:
            if char != '\n':
                carlines.append(char)
        chars.append(carlines)


def find_word(x, y, dirX, dirY):

    for letter in 'MAS':
        x = x + dirX
        y = y + dirY
        if x == -1 or y == -1 or x == len(chars) or y == len(chars):
            return 0
        if chars[x][y] != letter:
            return 0
    return 1


result = 0

for i in range(len(chars)):
    for j in range(len(chars[0])):
        if chars[i][j] == 'X':
            for dirI in range(-1, 2):
                for dirJ in range(-1, 2):
                    result += find_word(i, j, dirI, dirJ)
print(result)
