file = [line.strip().split() for line in open("input02.txt").readlines()]

"""Part One"""
res = 0
for line in file:
    op, me = line[0], line[1]
    mapped = chr(ord(op) - ord('A') + ord('X'))
    res += ord(me) - ord('X') + 1
    res += ((ord(me) - ord(mapped) + 1) % 3) * 3
print(res)

"""Part Two"""
res = 0
for line in file:
    op, outcome = line[0], line[1]
    mapped = chr(ord(op) - ord('A') + ord('X'))
    me = chr(ord('A') + (ord(outcome) - ord('X') + ((ord(op) - ord('B')) % 3)) % 3)
    res += ord(me) - ord('A') + 1
    res += (ord(outcome) - ord('X')) * 3
print(res)
