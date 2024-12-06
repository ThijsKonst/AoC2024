def check_line(line):
    for index in range(len(line)):
        new_line = [*line]
        del new_line[index]

        first, rest = new_line[0], new_line[1:]
        if first - rest[0] == 0:
            continue

        desc = first > rest[0]

        unsafe = False
        for x in rest:
            diff = (x - first)
            if (desc):
                diff *= -1

            if diff == 0:
                print("is Zero")
                unsafe = True
                break

            if diff < 1 or diff > 3:
                print(f"Diff too high: {diff}")
                unsafe = True
                break
            first = x

        if not unsafe:
            return True


with open('input.txt') as file:
    safe = 0
    for line in file.readlines():
        diff = 0
        nums = list(map(lambda x: int(x), line.split(' ')))
        if check_line(nums):
            safe += 1

    print(safe)
