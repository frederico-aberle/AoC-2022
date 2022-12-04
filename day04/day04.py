file = [line.strip().split(',') for line in open("input04.txt").readlines()]
file = [([int(x) for x in item[0].split('-')], [int(x) for x in item[1].split('-')]) for item in file]

"""Part One"""
res = 0
for line in file:
    first, second = line
    if (first[0] <= second[0] and first[1] >= second[1]) or (second[0] <= first[0] and second[1] >= first[1]):
        res += 1
print(res)

"""Part Two"""
cnt = 0
for line in file:
    first, second = line
    if first[1] < second[0] or second[1] < first[0]:
        cnt += 1
print(len(file)-cnt)
