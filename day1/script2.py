with open('input.txt') as file:
    leftList = []
    rightList = []
    for line in file:
        left, right = map(lambda x: int(x), line.split('   '))
        leftList += [left]
        rightList += [right]

    dist = 0
    for x in leftList:
        dist += x * rightList.count(x)

    print(dist)
