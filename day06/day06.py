file = [line.strip() for line in open("input06.txt").readlines()]

for line in file:
    """Part One"""
    for i in range(3, len(line)):
        if len(set(line[i-3:i+1])) == 4:
            print(i+1)
            break

    """Part Two"""
    for i in range(13, len(line)):
        if len(set(line[i-13:i+1])) == 14:
            print(i+1)
            break
