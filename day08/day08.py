file = [line.strip() for line in open("input08.txt").readlines()]

heights = [[int(x) for x in line] for line in file]
m = len(heights)
n = len(heights[0])

"""Part One"""
local_max_down = [[0 for j in range(n)] for i in range(m)]
local_max_right = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0 or i == m-1 or j == n-1:
            local_max_down[i][j] = 0
            local_max_right[i][j] = 0
        else:
            local_max_down[i][j] = max(local_max_down[i-1][j], heights[i-1][j])
            local_max_right[i][j] = max(local_max_right[i][j-1], heights[i][j-1])

local_max_up = [[0 for j in range(n)] for i in range(m)]
local_max_left = [[0 for j in range(n)] for i in range(m)]
for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        if i == 0 or j == 0 or i == m-1 or j == n-1:
            local_max_up[i][j] = 0
            local_max_left[i][j] = 0
        else:
            local_max_up[i][j] = max(local_max_up[i+1][j], heights[i+1][j])
            local_max_left[i][j] = max(local_max_left[i][j+1], heights[i][j+1])

result = 2 * (m + n) - 4
for i in range(1, m-1):
    for j in range(1, n-1):
        if heights[i][j] > min(local_max_up[i][j], local_max_down[i][j], local_max_left[i][j], local_max_right[i][j]):
            result += 1
print(result)

"""Part Two"""


def scenic_score(matrix, x, y):
    res = 1
    for i in range(x-1, -1, -1):
        if i == 0 or matrix[i][y] >= matrix[x][y]:
            res *= x - i
            break
    for i in range(x+1, m):
        if i == m-1 or matrix[i][y] >= matrix[x][y]:
            res *= x - i
            break
    for j in range(y-1, -1, -1):
        if j == 0 or matrix[x][j] >= matrix[x][y]:
            res *= y - j
            break
    for j in range(y+1, n):
        if j == n-1 or matrix[x][j] >= matrix[x][y]:
            res *= y - j
            break
    return res


result = 1
for i in range(1, m-1):
    for j in range(1, n-1):
        result = max(result, scenic_score(heights, i, j))
print(result)
