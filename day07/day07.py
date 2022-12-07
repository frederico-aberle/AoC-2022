file = [line.strip() for line in open("input07.txt").readlines()]

MAX_DIRE_SIZE = 100000
FILESYSTEM_SIZE = 70000000
MIN_UNUSED_SIZE = 30000000


class TreeNode:
    def __init__(self, val=0, parent=None, neighbours=None):
        self.val = val
        self.parent = parent
        self.neighbours = neighbours


root = TreeNode()
curr = root
i = 0
while i < len(file):
    line = file[i].split()
    comd = line[1]
    match comd:
        case 'cd':
            dire = line[2]
            match dire:
                case '/':
                    i += 1
                    continue
                case '..':
                    curr = curr.parent
                case _:
                    curr = curr.neighbours[dire]
        case 'ls':
            curr.neighbours = dict()

            i += 1
            line = file[i].split()
            kind = line[0]
            while kind != '$':
                name = line[1]
                match kind:
                    case 'dir':
                        curr.neighbours[name] = TreeNode(parent=curr)
                    case _:
                        curr.neighbours[name] = TreeNode(val=int(kind), parent=curr)
                i += 1
                if i >= len(file):
                    break
                line = file[i].split()
                kind = line[0]
            continue
    i += 1


def dfs_part_one(node, res):
    if not node.neighbours:
        return res
    for idx in node.neighbours.keys():
        neighbour = node.neighbours[idx]
        res = dfs_part_one(neighbour, res)
        node.val += neighbour.val
    if node.val <= MAX_DIRE_SIZE:
        res += node.val
    return res


def dfs_part_two(node, res):
    if not node.neighbours:
        return res
    for idx in node.neighbours.keys():
        neighbour = node.neighbours[idx]
        res = dfs_part_two(neighbour, res)
    if MIN_FREE_UP_SIZE <= node.val < res:
        res = node.val
    return res


"""PART ONE"""
result = dfs_part_one(root, 0)
print(result)

"""PART TWO"""
USED_SIZE = root.val
UNUSED_SIZE = FILESYSTEM_SIZE - USED_SIZE
MIN_FREE_UP_SIZE = MIN_UNUSED_SIZE - UNUSED_SIZE
print(dfs_part_two(root, USED_SIZE))
