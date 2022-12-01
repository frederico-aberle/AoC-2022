file = [line.strip() for line in open("input01.txt").readlines()]

"""Part One"""
res = float('-inf')
cal = 0
for line in file:
    if line == '':
        res = max(res, cal)
        cal = 0
        continue
    cal += int(line)
res = max(res, cal)
print(res)

"""Part Two"""
calories = []
cal = 0
for line in file:
    if line == '':
        calories.append(cal)
        cal = 0
        continue
    cal += int(line)
calories.append(cal)
print(sum(sorted(calories)[-3:]))
