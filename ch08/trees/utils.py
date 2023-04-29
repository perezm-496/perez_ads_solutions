"""Utilities for all trees."""


import lmrs


def descendants(v):
    pending = []
    descend_list = []
    pending.append(v)
    while pending:
        curr = pending.pop(0)
        for x in curr.children():
            pending.append(x)
            descend_list.append(x)
    return descend_list


def ancestors(v):
    """Returns a list of ancestors.
       Makes use ot the parent pointer.
       Notice that not all implementations use that pointer.\
    """
    curr = v
    ancest_list = []
    while curr.parent is not None:
        ancest_list.append(curr.parent)
        curr = curr.parent
    return ancest_list


def depth(v):
    curr = v
    depth_val = 0
    while curr.parent is not None:
        depth_val += 1
        curr = curr.parent
    return depth_val


def height(v):
    if not v.children():
        return 0
    else:
        return 1 + max([height(x) for x in v.children()])


def size(v):
    return 1 + len(descendants)


def show_node(v, lvl):
    if lvl > 0:
        txt = "      "*(lvl - 1)
        txt += "|---->"
        txt += str(v.key) + ":" + str(v.data)
        print(txt)
    else:
        print(str(v.key) + ":" + str(v.data))


def show(T):
    S = []  # New stack to store the nodes.
    S.append((0, T.root))
    while S:
        curr_lvl, curr = S.pop()
        show_node(curr, curr_lvl)
        for x in curr.children():
            S.append((curr_lvl + 1, x))


print("LMRS -- Mini test.")          
r = lmrs.LMRSNode(1, 1)
T = lmrs.LMRSTree(r)
show(T)
print("-"*10)
lmrs.add_vertex(T, 1, 11, 11)
lmrs.add_vertex(T, 11, 111, 111)
lmrs.add_vertex(T, 11, 112, 112)
lmrs.add_vertex(T, 111, 1111, 1111)
lmrs.add_vertex(T, 1111, 11111, 11111)
lmrs.add_vertex(T, 1, 12, 12)
lmrs.add_vertex(T, 12, 121, 121)
lmrs.add_vertex(T, 121, 1211, 1211)
lmrs.add_vertex(T, 12, 122, 122)
lmrs.add_vertex(T, 122, 1221, 1221)
lmrs.add_vertex(T, 12, 123, 123)
show(T)
print("-"*10)

print("Descendants")
for x in descendants(lmrs.search_key(T, 11)):
    print(x)

print("Ancestors")
for x in ancestors(lmrs.search_key(T, 1221)):
    print(x)

print(height(r))
