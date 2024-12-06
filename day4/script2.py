chars = []

with open('input.txt') as file:
    for line in file:
        carlines = []
        for char in line:
            if char != '\n':
                carlines.append(char)
        chars.append(carlines)


def check_mas(x, y):
    word = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            if chars[x+i][y+j] not in ["M", "S"]:
                return 0
            word.append(chars[x+i][y+j])
    print(word)
    if word.count('M') == 2 and word.count('S') == 2:
        print(word[0] != word[-1])
        if word[0] != word[-1]:
            return 1
    return 0


result = 0

for i in range(1, len(chars)-1):
    for j in range(1, len(chars[0])-1):
        if chars[i][j] == 'A':
            result += check_mas(i, j)
print(result)
