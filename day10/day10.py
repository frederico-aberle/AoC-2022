file = [line.strip().split() for line in open("input10.txt").readlines()]

"""Part One"""
cycle = 1
X = 1
res = 0
for line in file:
    instr_type = line[0]
    match instr_type:
        case 'noop':
            if cycle % 40 == 20:
                res += cycle * X
            cycle += 1
        case 'addx':
            if cycle % 40 == 19:
                res += (cycle + 1) * X
            elif cycle % 40 == 20:
                res += cycle * X
            X += int(line[1])
            cycle += 2
print(res)

"""Part Two"""
M = 6
N = 40
X = [1 for i in range(M*N)]
cycle = 1

for line in file:
    instr_type = line[0]
    match instr_type:
        case 'noop':
            if cycle >= len(X):
                break
            X[cycle] = X[cycle-1]
            cycle += 1
        case 'addx':
            if cycle >= len(X):
                break
            X[cycle] = X[cycle-1]
            if cycle+1 >= len(X):
                break
            X[cycle+1] = X[cycle-1] + int(line[1])
            cycle += 2

for i in range(M):
    for j in range(N):
        cycle = i*40+j+1
        # print(cycle, X[cycle-1])
        if X[cycle-1]-1 <= cycle-i*40-1 <= X[cycle-1]+1:
            print('#', end='')
        else:
            print('.', end='')
    print()
