import itertools

values = []
with open('input.txt') as file:
    for line in file.readlines():
        rule, elements = line.split(': ')
        values.append(
            (int(rule), list(map(lambda x: int(x), elements.split(' ')))))


def calculate(elements, operations):
    carry = elements[0]
    rest = elements[1:]
    for i in range(len(operations)):
        if operations[i]:
            carry *= rest[i]
        else:
            carry += rest[i]
    return carry


result = 0
for rule, elements in values:
    for op in itertools.product([True, False], repeat=len(elements)-1):
        if rule == calculate(elements, op):
            result += rule
            break
print(result)
