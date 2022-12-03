file = [line.strip() for line in open("input03.txt").readlines()]

"""Part One"""
res = 0
for line in file:
    comp_one = line[:len(line)//2]
    comp_two = line[len(line)//2:]
    common = list(set(comp_one).intersection(comp_two))[0]
    res += ord(common) - ord('a') + 1 if common.islower() else ord(common) - ord('A') + 27
print(res)

"""Part Two"""
res = 0
for i in range(len(file)//3):
    bag_one = file[3*i]
    bag_two = file[3*i+1]
    bag_thr = file[3*i+2]
    common = list(set(bag_one).intersection(bag_two).intersection(bag_thr))[0]
    res += ord(common) - ord('a') + 1 if common.islower() else ord(common) - ord('A') + 27
print(res)
