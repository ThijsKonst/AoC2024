rules_parsed = []
lines_parsed = []

with open('input.txt') as file:
    rules, lines = file.read().split('\n\n')
    for rule in rules.split('\n'):
        rules_parsed.append(
            list(map(lambda x: int(x.strip()), rule.split('|'))))
    for line in lines.split('\n'):
        if line != '':
            lines_parsed.append(
                list(map(lambda x: int(x.strip()), line.split(','))))


def check_all_rules(line):
    for first, second in relevant_rules(line):
        if not check_rules(first, second, line):
            return first, second
    return -1, -1


def check_rules(first, second, line):
    firsti = line.index(first)
    secondi = line.index(second)
    if firsti < secondi:
        return True

    return False


def relevant_rules(line):
    return [[first, second] for first, second in rules_parsed if first in line and second in line]


def reorder_list(line):
    while True:
        first, second = check_all_rules(line)
        if first == -1 and second == -1:
            return line
        line[line.index(first)], line[line.index(second)
                                      ] = line[line.index(second)], line[line.index(first)]


result = 0
for line in lines_parsed:
    error = False

    if check_all_rules(line) != (-1, -1):
        error = True
        reorder_list(line)

    if error:
        result += line[int(len(line)/2)]

print(result)
