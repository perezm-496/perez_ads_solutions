"""Array pointer implementation of a tree."""


class ArrayPntNode:
    """
       Node implementation for the array pointer tree.
    """

    def __init__(self, key, data, branch_factor=2, parent=None):
        self.child_array = [None]*branch_factor
        self.key = key
        self.data = data
        self.parent = parent
        self.branch_factor = branch_factor

    def children(self):
        children_list = []
        for x in self.child_array:
            if x is not None:
                children_list.append(x)
        return children_list

    def is_leaf(self):
        for x in self.child_array:
            if x is not None:
                return False
        return True

    def __str__(self):
        txt = "["
        txt += str(self.key)
        txt += ":" + str(self.data)
        txt += "]"
        return txt


class ArrayTree:
    """
    Class implementing a array of pointers tree.
    """

    def __init__(self, root):
        self.root = root

    def root(self):
        return self.root

    def size(self):
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


def search(T, target_key):
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


def add_vertex(T, parent_key, new_key, data):
    """
    Insert a new node with key child_key to the parent
    node with key parent_key with the associated data.
    """
    parent_node = search(T, parent_key)
    print(f"Parent node: {parent_node}")
    new_node = ArrayPntNode(new_key, data,
                            branch_factor=parent_node.branch_factor,
                            parent=parent_node)
    for j in range(parent_node.branch_factor):
        x = parent_node.child_array[j]
        if x is None:
            parent_node.child_array[j] = new_node
            return new_node
    return -1  # No space available
    # Opted for don't raise an Exception.

