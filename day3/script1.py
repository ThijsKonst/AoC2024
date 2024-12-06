import re
with open('input.txt') as file:
    result = 0
    for line in file.readlines():
        for occurance in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line):
            [numOne, numTwo] = re.findall(r'[0-9]{1,3}', occurance)
            result += int(numOne) * int(numTwo)
    print(result)
