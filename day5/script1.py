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


def check_rules(first, second, line):
    if first not in line or second not in line:
        return True
    firsti = line.index(first)
    secondi = line.index(second)
    if firsti < secondi:
        return True

    return False


result = 0
for line in lines_parsed:
    error = False
    for first, second in rules_parsed:
        if not check_rules(first, second, line):
            error = True
            break
    if not error:
        result += line[int(len(line)/2)]

print(result)
