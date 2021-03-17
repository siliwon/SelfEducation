tree = dict()


def get_parent(child):
    return 0 if not len(tree[child]) else 1 + get_parent(tree[child])


with open('input.txt', encoding='utf8') as inf:
    _ = int(inf.readline())
    for line in inf:
        child, parent = line.strip().split()
        tree[child] = parent
        tree[parent] = tree.get(parent, '')  # для родоначальника
[print(child, get_parent(child)) for child in sorted(tree)]
