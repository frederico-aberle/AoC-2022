file = [[line.strip().split()[0], int(line.strip().split()[1])] for line in open("input09.txt").readlines()]

# construct big enough grid
left_from_start = 0
right_from_start = 0
up_from_start = 0
down_from_start = 0
for line in file:
    dire, num = line
    match dire:
        case 'L':
            left_from_start += num
        case 'R':
            right_from_start += num
        case 'U':
            up_from_start += num
        case 'D':
            down_from_start += num
grid = [[False for j in range(left_from_start+right_from_start+1)] for i in range(up_from_start+down_from_start+1)]
s = [up_from_start, left_from_start]

"""Part One"""
h = s.copy()
t = s.copy()
grid[t[0]][t[1]] = True
for line in file:
    dire, num = line
    for i in range(num):
        h_old = h.copy()
        match dire:
            case 'L':
                h[1] -= 1
            case 'R':
                h[1] += 1
            case 'U':
                h[0] -= 1
            case 'D':
                h[0] += 1
        if abs(h[0]-t[0]) > 1 or abs(h[1]-t[1]) > 1:
            t = h_old
        grid[t[0]][t[1]] = True
print(sum(sum(row) for row in grid))

"""Part Two"""
knots = [s.copy() for i in range(10)]
grid[knots[-1][0]][knots[-1][1]] = True


def print_matrix():
    matrix = [['.' for j in range(left_from_start+right_from_start+1)] for i in range(up_from_start+down_from_start+1)]
    matrix[s[0]][s[1]] = 's'
    for i in range(len(knots)):
        knot = knots[i]
        matrix[knot[0]][knot[1]] = str(i)
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()
    print()


# print_matrix()
for line in file:
    dire, num = line
    for i in range(num):
        h = knots[0]
        match dire:
            case 'L':
                h[1] -= 1
            case 'R':
                h[1] += 1
            case 'U':
                h[0] -= 1
            case 'D':
                h[0] += 1
        for j in range(1, 10):
            t = knots[j]
            if abs(h[0]-t[0]) > 1 or abs(h[1]-t[1]) > 1:
                if h[0] < t[0]:
                    t[0] -= 1
                elif h[0] > t[0]:
                    t[0] += 1
                if h[1] < t[1]:
                    t[1] -= 1
                elif h[1] > t[1]:
                    t[1] += 1
            h = t
        grid[t[0]][t[1]] = True
    # print_matrix()

print(sum(sum(row) for row in grid))

"""
for i in range(len(grid)):
    row = grid[i]
    for j in range(len(row)):
        col = row[j]
        if i == s[0] and j == s[1]:
            print('s', end=" ")
        elif col:
            print('#', end=" ")
        else:
            print('.', end=" ")
    print()
"""
