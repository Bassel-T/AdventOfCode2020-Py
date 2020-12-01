class Day1Code:

    def __init__(self, isSecond):
        if isSecond:
            partTwo()
        else:
            partOne()



def partOne():
    numbers = list()

    # Read all inputs
    with open("inputs/day1.txt", "r") as file:
        line = file.readline()
        while line:
            numbers.append(int(line))
            line = file.readline()

    # Sort the array
    numbers.sort()

    # Create the lookup table
    table = [False] * (numbers[len(numbers) - 1] + 1)
    for i in numbers:
        table[i] = True

    # Run algorithm
    for i in numbers:
        if table[2020 - i]:
            print((2020 - i) * i)
            return


def partTwo():
    numbers = list()

    # Read all inputs
    with open("inputs/day1.txt", "r") as file:
        line = file.readline()
        while line:
            numbers.append(int(line))
            line = file.readline()

    # Sort the array
    numbers.sort()

    # Create the lookup table
    table = [False] * (numbers[len(numbers) - 1] + 1)
    for i in numbers:
        table[i] = True

    # Run algorithm
    for i in numbers:
        for j in numbers:
            if i + j >= 2020:
                break

            if table[2020 - i - j]:
                print((2020 - i - j) * i * j)
                return