# Problem Statement
# given multiple disjointed trees , return the root of the tree that has maximum elements.
# if two trees share same no of elements return the tree which has minimum root value
# trees are represented in key value pair with key being the child and value being the parent
# a single parent can have multiple child's , and every child can have only single parent
# eg : for a tree as  { 2:4 , 3:1 } output will be 1 as 1<4 and both trees have same elements

tree = {2: 4, 3: 1, 5: 4, 6: 1, 7: 6, 8: 7, 11: 0, 12: 0, 13: 0, 14: 0}

tree_rooted = {}
root_items = {}


def get_root(c):
    if c in tree.keys():
        return get_root(tree[c])
    else:
        return c


def get_longest_tree():
    for k, v in tree.items():
        tree_rooted[k] = get_root(v)


def get_root_items():
    for k, v in tree_rooted.items():
        if v not in root_items.keys():
            root_items[v] = [k]
        else:
            root_items[v].append(k)


def get_len_root():
    for k, v in root_items.items():
        root_items[k] = len(root_items[k])


def get_the_best_root():
    maximum = -1
    for k, v in root_items.items():
        if v > maximum:
            maximum = v

    final_roots = []
    for k, v in root_items.items():
        if v == maximum:
            final_roots.append(k)

    return min(final_roots)


get_longest_tree()
get_root_items()
get_len_root()
print('The root with maximum no of elements is : '+str(get_the_best_root()))
