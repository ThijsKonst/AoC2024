with open('input.txt') as file:
    leftList = []
    rightList = []
    for line in file:
        left, right = map(lambda x: int(x), line.split('   '))
        leftList += [left]
        rightList += [right]

    leftList.sort()
    rightList.sort()
    dist = 0
    for x in range(len(leftList)):
        dist += abs(leftList[x] - rightList[x])

    print(dist)
