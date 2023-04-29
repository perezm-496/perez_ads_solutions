"""Left most right sibling implemantation of a tree."""


class LMRSNode:
    """
     Node designed to be used in a left most right sibling
    implementation of a tree.
    """

    def __init__(self, key, data, sibling=None, lmchild=None, parent=None):
        self.key = key
        self.data = data
        self.sibling = sibling
        self.lmchild = lmchild
        self.parent = parent

    def children(self):
        child_list = []
        curr_child = self.lmchild
        while curr_child is not None:
            child_list.append(curr_child)
            curr_child = curr_child.sibling
        return child_list

    def is_leaf(self):
        return self.lmchild is not None

    def __str__(self):
        txt = "["
        txt += str(self.key)
        txt += ":" + str(self.data)
        txt += "]"
        return txt


class LMRSTree:
    """
    Class implementing the left most right sibling of a tree.
    """

    def __init__(self, root):
        self.root = root

    def root(self):
        return self.root

    def size(self):
        # Start a deepth first traversal.
        S = []  # New stack
        S.append(self.root)
        curr_size = 0
        while len(S) != 0:
            next = S.pop()
            curr_size += 1
            curr_child = next.lmchild
            while curr_child is not None:
                S.append(curr_child)
                curr_child = curr_child.sibling
        return curr_size

    def is_root(self, v):
        return v.key == self.root.key

    def empty(self):
        return self.root is None


def search_key(T, target_key):
    """Returns the node with key = target_key."""
    # Uses depth first search
    S = []  # New Stack
    S.append(T.root)
    while S:
        curr = S.pop()
        if curr.key == target_key:
            return curr
        else:
            for x in curr.children():
                S.append(x)
    return None


def add_vertex(T, parent_key, child_key, data):
    """Inserts a new node with key child_key to the
       parent node with parent_key and associate to the
       data."""
    parent_node = search_key(T, parent_key)
    new_node = LMRSNode(child_key, data, parent=parent_node)
    curr = parent_node.lmchild
    if curr is None:
        parent_node.lmchild = new_node
        return new_node
    while curr.sibling is not None:
        curr = curr.sibling
    curr.sibling = new_node
    return new_node


if __name__ == "__main__":
    n = LMRSNode(0, "zero")
    T = LMRSTree(n)
    r = T.root
    print(f"root key {r.key}")
    add_vertex(T, 0, 10, "diez")
    add_vertex(T, 0, 20, "veinte")
    add_vertex(T, 10, 110, "1-1-0")
    add_vertex(T, 10, 210, "2-1-0")
    add_vertex(T, 20, 120, "1-2-0")
    for x in r.children():
        print(x)
        for y in x.children():
            print(y)
