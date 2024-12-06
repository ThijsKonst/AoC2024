import re
with open('input.txt') as file:
    result = 0
    for line in file.readlines():
        print(line)
        for part in line.split("do()"):
            to_check = part.split("don't()")[0]
            print(to_check)
            for occurance in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', to_check):
                [numOne, numTwo] = re.findall(r'[0-9]{1,3}', occurance)
                result += int(numOne) * int(numTwo)
    print(result)
