file = open("input05.txt")

# construction of base
rowBase = 8
colBase = 9
base1 = [[] for i in range(colBase)]
for row in range(rowBase):
    line = file.readline()
    for col in range(len(line)//4):
        c = line[4*col+1]
        if c.isalpha():
            base1[col].append(c)
for col in base1:
    col.reverse()
base2 = [col.copy() for col in base1]

# reading blank lines before instructions
for i in range(2):
    file.readline()

# reading instructions
instructions = [s.split() for s in file.readlines()]

# simulation
for instruction in instructions:
    n, orig, dest = tuple(map(int, [instruction[1], instruction[3], instruction[5]]))
    """Part One"""
    for i in range(n):
        base1[dest-1].append(base1[orig-1].pop())
    """Part Two"""
    base2[dest - 1].extend(base2[orig - 1][-n:])
    del base2[orig - 1][-n:]

# reading result
res1 = ""
res2 = ""
for i in range(colBase):
    res1 += base1[i].pop()
    res2 += base2[i].pop()
print(res1)
print(res2)
