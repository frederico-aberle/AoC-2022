file = open("input01.txt")
t = int(file.readline())
for i in range(t):
    a, b = map(int, file.readline().split())
    print(a, b)
